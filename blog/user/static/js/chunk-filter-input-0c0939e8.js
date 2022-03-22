System.register(["./chunk-vendor.js","./chunk-frameworks.js"],(function(e){"use strict";var t,s,i,r,n,a,o,u,l,h;return{setters:[function(e){t=e._,s=e.t,i=e.f,r=e.b,n=e.d,a=e.u},function(e){o=e.m,u=e.d,l=e.f,h=e.a}],execute:function(){class BaseFilterElement extends HTMLElement{constructor(){super(...arguments),this.showAllQualifiersIfNoneMatch=!0,this.fuzzyMatchQualifiers=!1,this.showSubmissionOptionIfInvalidSearchTerms=!1,this.suggestionsTitle="Available filters",this.spaceBetweenValueAndDescription=!0,this.selectorOfElementToActivateOnBlur=null}async cachedJSON(e){const t=await fetch(e,{headers:{"X-Requested-With":"XMLHttpRequest",Accept:"application/json"}});if(!t.ok){const e=new Error,s=t.statusText?" "+t.statusText:"";throw e.message=`HTTP ${t.status}${s}`,e}return t.json()}fetchQualifierSuggestions(){const e="data-suggestable-qualifiers",t=this.searchInput.getAttribute(e);if(null===t)throw new Error(`\n        ${e} is missing from ${this.searchInput.getAttribute("data-target")}.\n        Either add it or override fetchQualifierSuggestions.\n      `);return JSON.parse(t)}hideFilterSuggestions(){u(this.searchForm),this.autocompleteDropdown.hidden=!0,this.searchInput.setAttribute("aria-expanded","false")}updateFilterSuggestionResults(){const e=this.searchInput.value,t=(e.slice(0,this.searchInput.selectionEnd).match(/("[^"]+"?|\S)+$/)||[""])[0].replace(/"/g,"");this.autocompleteDropdown.hidden=!1,this.searchInput.setAttribute("aria-expanded","true");const[s,i]=t.split(":");null!=i?this.renderValueSuggestions(s,i):this.renderQualifierSuggestions(s),e.trim().length>0&&(!this.invalidSearchTerms()||this.showSubmissionOptionIfInvalidSearchTerms)&&!this.searchMatchesDefault()?(this.clearButton&&(this.clearButton.hidden=!1),l(this.searchForm)):(this.clearButton&&(this.clearButton.hidden=!0),h(this.searchForm))}handleSelectedSuggestionResultEvent(e){const t=e.target;if(t.hasAttribute("data-search"))return void this.searchForm.submit();let s=t.getAttribute("data-value");":"!==s[s.length-1]&&(s+=" ");const r=this.searchInput.value.slice(0,this.searchInput.selectionEnd).replace(/\S+$/,""),n=this.searchInput.value.slice(this.searchInput.selectionEnd),a=" "!==n[0]?" ":"";this.searchInput.value=r+s+a+n,e.preventDefault(),this.searchInput.focus();const o=r.length+s.length;this.searchInput.setSelectionRange(o,o),i(this.searchInput,"input")}handleFormKeydownEvent(e){if("Enter"===e.detail.hotkey){if(""!==this.searchInput.value.trim())return;if(this.autocompleteResults.querySelector(".js-filter-loading"))return;if(this.autocompleteResults.querySelector(".js-navigation-item.navigation-focus"))return;this.searchForm.submit()}}clear(){this.searchInput.value=this.getDefaultSearch(),0===this.getInitialValue().trim().length?this.updateFilterSuggestionResults():this.searchForm.submit()}renderQualifierSuggestions(e){this.showAllQualifiersIfNoneMatch?this.renderMatchingOrAllQualifierSuggestions(e):this.renderMatchingQualifierSuggestions(e)}renderMatchingOrAllQualifierSuggestions(e){const t=this.fetchQualifierSuggestions(),s=this.filterSuggestionsList(t,e,{fuzzy:this.fuzzyMatchQualifiers}).then((e=>0===e.length?t:e));this.renderSuggestionDropdown(s)}renderMatchingQualifierSuggestions(e){const t=this.filterSuggestionsList(this.fetchQualifierSuggestions(),e,{fuzzy:this.fuzzyMatchQualifiers});this.renderSuggestionDropdown(t)}renderValueSuggestions(e,t){const s=this.fetchMatchingSuggestions(e,t);this.renderSuggestionDropdown(s)}async fetchMatchingSuggestions(e,t){const s=this.fetchSuggestionsForQualifier(e);return(await this.filterSuggestionsList(s,t)).map((t=>({value:`${e}:${t.value}`,description:t.description})))}async filterSuggestionsList(e,t,{fuzzy:s}={fuzzy:!0}){const i=await e,r=t.trim();return r&&0!==r.length?i.filter((e=>s?e.value.includes(r):e.value.startsWith(r))):i}renderSuggestionDropdown(e){r(n`
        <div>
          ${this.renderSearchWarningIfRequired()}
          ${this.shouldRenderSubmissionOption()?this.renderSearchSuggestion():""}
          ${a(this.renderSuggestionList(e),this.renderLoadingItem())}
        </div>
      `,this.autocompleteResults),this.postDropdownRender()}renderSearchWarningIfRequired(){const e=this.invalidSearchTerms();return e&&0!==e.length?n`
      <div class="color-bg-warning color-text-secondary ml-n2 mr-n2 mt-n1 py-1 px-2 js-alert-search-warning-container">
        Sorry, we don't support the <span class="text-bold">${e}</span> filter yet.
      </div>
    `:""}postDropdownRender(){}renderSearchSuggestion(){const e=this.searchInput.value.trim();return 0===e.length?n``:n`
      <div class="border-bottom-0 rounded-1 py-1 px-2 mx-0 mb-1 js-navigation-item" data-search="true">
        <span class="text-bold">${e}</span> - submit
      </div>
    `}searchMatchesDefault(){return this.searchInput.value.trim()===this.getDefaultSearch().trim()}getInitialValue(){const e="data-initial-value",t=this.searchInput.getAttribute(e);if(null===t)throw new Error(e+" is missing from search input");return t}getDefaultSearch(){const e="data-default-value",t=this.searchInput.getAttribute(e);if(null===t)throw new Error(e+" is missing from search input");return t}renderSuggestionsTitle(){return n`<h6 class="width-full text-normal border-bottom color-bg-primary color-text-secondary py-2 mb-2">
      ${this.suggestionsTitle}
    </h6>`}async renderSuggestionList(e){const t=(await e).map((e=>n`
          <div
            class="border-bottom-0 rounded-1 py-1 px-2 mx-0 mb-1 js-navigation-item"
            data-value="${e.value}"
          >
            <span class="text-bold">${e.value}</span>${this.spaceBetweenValueAndDescription?" ":""}<span
              class="autocomplete-text-qualifier color-text-tertiary"
              >${e.description}</span
            >
          </div>
        `));return t.length&&t.unshift(this.renderSuggestionsTitle()),t}renderLoadingItem(){return n`
      ${this.renderSuggestionsTitle()}
      <span class="js-filter-loading">loading...</span>
    `}handleSearchBlur(){this.hideFilterSuggestions(),this.selectorOfElementToActivateOnBlur&&h(document.querySelector(this.selectorOfElementToActivateOnBlur))}inputKey(e){"Escape"===e.key&&this.handleSearchBlur()}shouldRenderSubmissionOption(){return this.showSubmissionOptionIfInvalidSearchTerms||!this.invalidSearchTerms()}}e("B",BaseFilterElement),t([s],BaseFilterElement.prototype,"autocompleteDropdown",void 0),t([s],BaseFilterElement.prototype,"autocompleteResults",void 0),t([s],BaseFilterElement.prototype,"clearButton",void 0),t([s],BaseFilterElement.prototype,"searchForm",void 0),t([s],BaseFilterElement.prototype,"searchInput",void 0),t([function(e={}){return(t,s,i)=>{i.value=o(i.value,e),Object.defineProperty(t,s,i)}}()],BaseFilterElement.prototype,"cachedJSON",null)}}}));
//# sourceMappingURL=chunk-filter-input-b7e6cfc7.js.map