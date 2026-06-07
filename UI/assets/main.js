window.addEventListener("load", () => {
  // Initialize Lucide Icons
  lucide.createIcons();

  // Floating animation
  gsap.to(".OPTIMUS", {
    y: -15,
    duration: 2,
    repeat: -1,
    yoyo: true,
    ease: "power1.inOut",
  });

  // Delayed startup sound
  // setTimeout(async () => {
  //   await eel.playOptimusInitialised()();
  // }, 1200);

  // Core pulse
  gsap.to(".core", {
    scale: 1.08,
    duration: 1.8,
    repeat: -1,
    yoyo: true,
    ease: "sine.inOut",
  });

  // Dot Orbit
  // gsap.to(".dot", {
  //   rotation: 360,
  //   transformOrigin: "250px 0px",
  //   repeat: -1,
  //   duration: 5,
  //   ease: "linear",
  // });

  // Status panel animation
  // gsap.from(".status", {
  //   x: 100,
  //   opacity: 0,
  //   duration: 1.5,
  //   ease: "power4.out",
  // });

  // Title Animation
  gsap.from(".title", {
    opacity: 0,
    y: 30,
    duration: 1.5,
    ease: "power4.out",
  });

  // gsap.from(".subtitle", {
  //   opacity: 0,
  //   y: 20,
  //   duration: 2,
  //   delay: 0.3,
  //   ease: "power4.out",
  // });

  // HUD line flicker
  gsap.to(".hud-line", {
    opacity: 0.2,
    repeat: -1,
    yoyo: true,
    stagger: 0.2,
    duration: 0.6,
  });

  /* =========================
   SIRI WAVE
========================= */

  const siriWaveSection = document.getElementById("SiriWave");

  const optimusSection = document.querySelector(".OPTIMUS");

  const micBtn = document.querySelector(".mic-btn");

  // CREATE WAVE

  const siriWave = new SiriWave({
    container: document.querySelector(".siri-container"),
    width: 700,
    height: 250,
    style: "ios9",
    speed: 0.12,
    amplitude: 1,
    autostart: true,
    cover: false,
  });

  // siriWave.start();

  // MIC CLICK EVENT
  /* =========================
   MIC BUTTON CLICK
========================= */

  // let listening = false;

  // micBtn.addEventListener("click", () => {
  //   if (!listening) {
  //     listening = true;

  //     // =========================
  //     // HIDE OPTIMUS
  //     // =========================

  //     gsap.to(".OPTIMUS", {
  //       opacity: 0,
  //       scale: 0.7,
  //       duration: 0.8,
  //       ease: "power4.inOut",
  //       onComplete: () => {
  //         optimusSection.style.visibility = "hidden";
  //       },
  //     });

  //     eel.playAssistantSound()

  //     // =========================
  //     // SHOW SIRI WAVE
  //     // =========================

  //     siriWaveSection.style.visibility = "visible";

  //     gsap.to("#SiriWave", {
  //       opacity: 1,
  //       duration: 1,
  //       delay: 1,
  //       ease: "power4.out",
  //     });

  //     eel.takeCommand()()
  //   } else {
  //     listening = false;

  //     // =========================
  //     // HIDE SIRI WAVE
  //     // =========================

  //     gsap.to("#SiriWave", {
  //       opacity: 0,
  //       duration: 0.8,
  //       ease: "power4.inOut",
  //       onComplete: () => {
  //         siriWaveSection.style.visibility = "hidden";
  //       },
  //     });

  //     eel.playOptimusSwitchUp()

  //     // =========================
  //     // SHOW OPTIMUS
  //     // =========================

  //     optimusSection.style.visibility = "visible";

  //     gsap.to(".OPTIMUS", {
  //       opacity: 1,
  //       scale: 1,
  //       duration: 1,
  //       delay: .7,
  //       ease: "power4.out",
  //     });
  //   }
  // });

  /* =========================
   MIC BUTTON CLICK
========================= */

  micBtn.addEventListener("click", async () => {
    // Prevent Multiple Clicks
    micBtn.disabled = true;

    // =========================
    // HIDE OPTIMUS
    // =========================

    gsap.to(".OPTIMUS", {
      opacity: 0,
      scale: 0.7,
      duration: 0.8,
      ease: "power4.inOut",
      onComplete: () => {
        optimusSection.style.visibility = "hidden";
      },
    });

    // =========================
    // PLAY ACTIVATION SOUND
    // =========================

    await eel.playAssistantSound()();

    // =========================
    // SHOW SIRI WAVE
    // =========================

    siriWaveSection.style.visibility = "visible";

    gsap.to("#SiriWave", {
      opacity: 1,
      duration: 1,
      ease: "power4.out",
    });

    // =========================
    // START LISTENING
    // =========================

    let command = await eel.manualCommand()();

    console.log("User Said:", command);

    // =========================
    // HIDE SIRI WAVE
    // =========================

    gsap.to("#SiriWave", {
      opacity: 0,
      duration: 0.8,
      ease: "power4.inOut",
      onComplete: () => {
        siriWaveSection.style.visibility = "hidden";
      },
    });

    // =========================
    // PLAY SWITCH SOUND
    // =========================

    // await eel.playOptimusSwitchUp()();

    // =========================
    // SHOW OPTIMUS AGAIN
    // =========================

    optimusSection.style.visibility = "visible";

    gsap.to(".OPTIMUS", {
      opacity: 1,
      scale: 1,
      duration: 1,
      ease: "power4.out",
    });

    // =========================
    // ENABLE BUTTON AGAIN
    // =========================

    micBtn.disabled = false;
  });
});
