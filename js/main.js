// ShineNova — small, dependency-free behaviors
(function () {
  const header = document.querySelector('.header');
  const menuBtn = document.querySelector('.menu-btn');

  // Sticky header hairline once scrolled
  const onScroll = () => header.classList.toggle('is-stuck', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Hero video: plays once (messy → clean) and holds on the clean room.
  // One button pauses, resumes, or replays. Reduced-motion and Save-Data visitors
  // see the clean room and can press play themselves.
  const video = document.querySelector('.hero__video');
  const vctl = document.querySelector('.vctl');
  if (video && vctl) {
    const calm = matchMedia('(prefers-reduced-motion: reduce)').matches ||
      (navigator.connection && navigator.connection.saveData);
    const setState = (state) => {
      vctl.dataset.state = state;
      const verb = { playing: 'Pause', paused: 'Play', ended: 'Replay' }[state];
      vctl.setAttribute('aria-label', verb + ' the before-and-after video');
    };
    const load = () => {
      if (video.src) return;
      video.src = matchMedia('(max-width: 900px)').matches ? video.dataset.srcSm : video.dataset.srcLg;
    };
    let userPaused = calm;
    video.addEventListener('play', () => setState('playing'));
    video.addEventListener('pause', () => { if (!video.ended) setState('paused'); });
    video.addEventListener('ended', () => setState('ended'));
    vctl.addEventListener('click', () => {
      load();
      if (video.ended) { video.currentTime = 0; video.play(); userPaused = false; }
      else if (video.paused) { video.play(); userPaused = false; }
      else { video.pause(); userPaused = true; }
    });
    // Browsers pause video in background tabs; pick up where it left off when the tab is shown
    document.addEventListener('visibilitychange', () => {
      if (!document.hidden && video.src && video.paused && !video.ended && !userPaused) video.play().catch(() => {});
    });

    if (calm) {
      video.poster = video.dataset.after;
      setState('paused');
    } else {
      load();
      video.preload = 'auto';
      video.play().catch(() => setState('paused'));
    }
  }

  // Mobile menu
  if (menuBtn) {
    menuBtn.addEventListener('click', () => {
      const open = header.classList.toggle('is-open');
      menuBtn.setAttribute('aria-expanded', String(open));
    });
  }

  // Mark the current page in the nav
  const here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav a').forEach((a) => {
    if (a.getAttribute('href') === here) a.setAttribute('aria-current', 'page');
  });

  // Quote / contact forms → Web3Forms (paste your access key in the hidden input)
  document.querySelectorAll('form[data-lead-form]').forEach((form) => {
    const status = form.querySelector('.form-status');
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const key = form.querySelector('input[name="access_key"]');
      const btn = form.querySelector('button[type="submit"]');
      const show = (msg, isError) => {
        if (!status) return;
        status.textContent = msg;
        status.classList.add('is-visible');
        status.classList.toggle('is-error', !!isError);
      };
      // Required name/phone, valid email if given (the form is novalidate, so check here)
      const bad = [...form.querySelectorAll('input, select, textarea')].find((el) => !el.checkValidity());
      if (bad) {
        const label = form.querySelector(`label[for="${bad.id}"]`);
        const name = label ? label.firstChild.textContent.trim() : 'this field';
        show(bad.value ? `Please check your ${name.toLowerCase()}.` : `Please add your ${name.toLowerCase()} so we can send your quote.`, true);
        bad.focus();
        return;
      }
      if (!key || key.value === 'YOUR_WEB3FORMS_KEY') {
        show('Demo mode: the form is wired up — add your Web3Forms key in the HTML to receive leads by email.', false);
        return;
      }
      btn.disabled = true;
      try {
        const res = await fetch('https://api.web3forms.com/submit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(Object.fromEntries(new FormData(form))),
        });
        const data = await res.json();
        if (data.success) {
          show("Thanks! We'll text or email your quote within the hour (during business hours).", false);
          form.reset();
        } else {
          show('Something went wrong sending your request. Please call us instead.', true);
        }
      } catch {
        show('Could not reach the server. Please call or email us.', true);
      } finally {
        btn.disabled = false;
      }
    });
  });

  // Footer year
  document.querySelectorAll('[data-year]').forEach((el) => (el.textContent = new Date().getFullYear()));
})();
