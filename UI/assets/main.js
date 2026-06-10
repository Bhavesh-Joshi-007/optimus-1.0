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

  // Core pulse
  gsap.to(".core", {
    scale: 1.08,
    duration: 1.8,
    repeat: -1,
    yoyo: true,
    ease: "sine.inOut",
  });

  // Title Animation
  gsap.from(".title", {
    opacity: 0,
    y: 30,
    duration: 1.5,
    ease: "power4.out",
  });

  // HUD line flicker
  gsap.to(".hud-line", {
    opacity: 0.2,
    repeat: -1,
    yoyo: true,
    stagger: 0.2,
    duration: 0.6,
  });
  
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

  micBtn.addEventListener("click", async () => {
    // Prevent Multiple Clicks
    micBtn.disabled = true;

    gsap.to(".OPTIMUS", {
      opacity: 0,
      scale: 0.7,
      duration: 0.8,
      ease: "power4.inOut",
      onComplete: () => {
        optimusSection.style.visibility = "hidden";
      },
    });

    await eel.playAssistantSound()();

    siriWaveSection.style.visibility = "visible";

    gsap.to("#SiriWave", {
      opacity: 1,
      duration: 1,
      ease: "power4.out",
    });

    let command = await eel.manualCommand()();

    console.log("User Said:", command);

    gsap.to("#SiriWave", {
      opacity: 0,
      duration: 0.8,
      ease: "power4.inOut",
      onComplete: () => {
        siriWaveSection.style.visibility = "hidden";
      },
    });

    optimusSection.style.visibility = "visible";

    gsap.to(".OPTIMUS", {
      opacity: 1,
      scale: 1,
      duration: 1,
      ease: "power4.out",
    });

    micBtn.disabled = false;
  });
});
