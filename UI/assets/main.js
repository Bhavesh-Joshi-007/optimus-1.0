// Floating animation
gsap.to(".jarvis", {
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

// Dot Orbit
// gsap.to(".dot", {
//   rotation: 360,
//   transformOrigin: "250px 0px",
//   repeat: -1,
//   duration: 5,
//   ease: "linear",
// });

// Status panel animation
gsap.from(".status", {
  x: 100,
  opacity: 0,
  duration: 1.5,
  ease: "power4.out",
});

// Title Animation
gsap.from(".title", {
  opacity: 0,
  y: 30,
  duration: 1.5,
  ease: "power4.out",
});

gsap.from(".subtitle", {
  opacity: 0,
  y: 20,
  duration: 2,
  delay: 0.3,
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
