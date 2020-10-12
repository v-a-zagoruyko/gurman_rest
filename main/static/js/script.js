const images = [
  {
    src: "https://xn----7sbblh9beecscegov.xn--p1ai/static/images/gallery/1.jpg",
    w: 0,
    h: 0,
  },
  {
    src: "https://xn----7sbblh9beecscegov.xn--p1ai/static/images/gallery/2.jpg",
    w: 0,
    h: 0,
  },
  {
    src: "https://xn----7sbblh9beecscegov.xn--p1ai/static/images/gallery/3.jpg",
    w: 0,
    h: 0,
  },
  {
    src: "https://xn----7sbblh9beecscegov.xn--p1ai/static/images/gallery/4.jpg",
    w: 0,
    h: 0,
  },
  {
    src: "https://xn----7sbblh9beecscegov.xn--p1ai/static/images/gallery/5.jpg",
    w: 0,
    h: 0,
  },
  {
    src: "https://xn----7sbblh9beecscegov.xn--p1ai/static/images/gallery/6.jpg",
    w: 0,
    h: 0,
  },
  {
    src: "https://xn----7sbblh9beecscegov.xn--p1ai/static/images/gallery/7.jpg",
    w: 0,
    h: 0,
  },
  {
    src: "https://xn----7sbblh9beecscegov.xn--p1ai/static/images/gallery/8.jpg",
    w: 0,
    h: 0,
  },
  {
    src: "https://xn----7sbblh9beecscegov.xn--p1ai/static/images/gallery/9.jpg",
    w: 0,
    h: 0,
  },
  {
    src:
      "https://xn----7sbblh9beecscegov.xn--p1ai/static/images/gallery/10.jpg",
    w: 0,
    h: 0,
  },
];

const options = {
  index: 0,
  closeOnScroll: false,
};

const galleryContainer = document.querySelectorAll(".pswp")[0];
const galleryToggle = document.getElementById("run-gallery");

galleryToggle.addEventListener("click", (e) => {
  e.preventDefault();

  let gallery = new PhotoSwipe(
    galleryContainer,
    PhotoSwipeUI_Default,
    images,
    options
  );
  gallery.listen("gettingData", function (index, item) {
    if (item.w < 1 || item.h < 1) {
      // unknown size
      var img = new Image();
      img.onload = function () {
        item.w = this.width;
        item.h = this.height;
        gallery.invalidateCurrItems();
        gallery.updateSize(true);
      };
      img.src = item.src;
    }
  });

  gallery.init();
});
