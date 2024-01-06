// This is the "Offline page" service worker

// Add this below content to your HTML page inside a <script type="module"></script> tag, or add the js file to your page at the very top to register service worker
// If you get an error about not being able to import, double check that you have type="module" on your <script /> tag

/*
 This code uses the pwa-update web component https://github.com/pwa-builder/pwa-update to register your service worker,
 tell the user when there is an update available and let the user know when your PWA is ready to use offline.
*/

import 'https://cdn.jsdelivr.net/npm/@pwabuilder/pwaupdate';

const el = document.createElement('pwa-update');
document.body.appendChild(el);

//This is the "Offline page" service worker

//Add this below content to your HTML page, or add the js file to your page at the very top to register service worker
// if (navigator.serviceWorker.controller) {
//   console.log('[PWA Builder] active service worker found, no need to register')
// } else {
//   //Register the ServiceWorker
//   navigator.serviceWorker.register('pwabuider-sw.js', {
//     scope: './'
//   }).then(function(reg) {
//     console.log('Service worker has been registered for scope:'+ reg.scope);
//   });
// }
