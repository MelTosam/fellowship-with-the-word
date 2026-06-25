const CACHE_NAME = 'fwtw-cache-v1';
const urlsToCache = [
    '/',
    '/devotionals',
    '/sermons',
    '/bible',
    '/about',
    '/contact',
    '/give',
    '/profile',
    '/static/css/style.css'
];

self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
            .then(function(response) {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            }
        )
    );
});
