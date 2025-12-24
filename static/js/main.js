import { initLoading } from './loading.js';
import { loadSettingsIntoUI } from './settings.js';
import { setupDragAndDrop } from './dragdrop.js';
import { initJoiner } from './joiner.js';
import { initVC } from './vc.js';
import { initLeaver } from './leaver.js';
import { initPfp } from './pfp.js';
import { connectToEventStream } from './events.js';
import { initTabs } from './tabs.js';

document.addEventListener("DOMContentLoaded", async () => {
    await initLoading();
    initTabs();
    loadSettingsIntoUI();
    setupDragAndDrop();
    initJoiner();
    initVC();
    initLeaver();
    initPfp();
    connectToEventStream();
});
