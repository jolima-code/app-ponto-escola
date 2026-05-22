self.addEventListener("install", function(event) {
    console.log("PWA instalado");
});

self.addEventListener("fetch", function(event) {
    event.respondWith(fetch(event.request));
});