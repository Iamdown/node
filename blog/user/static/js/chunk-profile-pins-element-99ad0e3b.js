System.register(["./chunk-vendor.js"],(function(){"use strict";var t,e,i,o;return{setters:[function(n){t=n._,e=n.t,i=n.g,o=n.c}],execute:function(){let n=class ProfilePinsElement extends HTMLElement{constructor(){super(...arguments),this.autoreloadCount=100}loadMorePinnableItems(){this.remotePagination.hasNextPage&&0!==this.autoreloadCount&&(this.autoreloadCount--,this.remotePagination.addEventListener("remote-pagination-load",this.loadMorePinnableItems.bind(this),{once:!0}),this.remotePagination.loadNextPage())}filter(){this.input.dispatchEvent(new Event("change",{bubbles:!0}))}async limitPins(){await Promise.resolve();const t=this.checkboxes,e=t.filter((t=>t.checked)).length,i=parseInt(this.getAttribute("max"),10);for(const s of t)s.disabled=e===i&&!s.checked;const o=this.limitNotice.getAttribute("data-remaining-label")||"",n=i-e;this.limitNotice.textContent=`${n} ${o}`,this.limitNotice.classList.toggle("color-text-danger",n<1)}disableLastCheckedInput(){const t=this.filterTypeInputs.filter((t=>t.checked));for(const e of t)e.disabled=1===t.length}setFilteringLogic(){const t=this.filterTypeInputs.filter((t=>t.checked)).map((t=>t.value));this.filterInput.filter=(e,i,o)=>{const n=o.toLowerCase().trim();if(e.querySelector("input:checked"))return{match:!0};const s=!n||i.toLowerCase().indexOf(n.toLowerCase())>-1,r=e.getAttribute("data-pinnable-type"),a=!(t.length>0&&r)||t.includes(r);return{match:s&&a}}}};t([e],n.prototype,"limitNotice",void 0),t([e],n.prototype,"filterInput",void 0),t([e],n.prototype,"input",void 0),t([i],n.prototype,"filterTypeInputs",void 0),t([e],n.prototype,"remotePagination",void 0),t([e],n.prototype,"form",void 0),t([i],n.prototype,"checkboxes",void 0),n=t([o],n)}}}));
//# sourceMappingURL=chunk-profile-pins-element-eb7411a7.js.map