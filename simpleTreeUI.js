// Use the jQuery instance from the global scope (loaded via CDN in index.html)
// instead of importing it as a module
const $ = window.jQuery;

var _defaults = {
  // Optionally provide here the jQuery element that you use as the search box for filtering the tree. simpleTree then takes control over the provided box, handling user input
  searchBox: undefined,

  // Search starts after at least 3 characters are entered in the search box
  searchMinInputLength: 3,

  // Number of pixels to indent each additional nesting level
  indentSize: 25,

  // Show child count badges?
  childCountShow: true,

  // Symbols for expanded and collapsed nodes that have child nodes
  symbols: {
    collapsed: "▶",
    expanded: "▼",
  },

  // these are the CSS class names used on various occasions. If you change these names, you also need to provide the corresponding CSS class
  css: {
    childrenContainer: "simpleTree-childrenContainer",
    childCountBadge:
      "simpleTree-childCountBadge badge badge-pill badge-secondary",
    highlight: "simpleTree-highlight",
    indent: "simpleTree-indent",
    label: "simpleTree-label",
    mainContainer: "simpleTree-mainContainer",
    nodeContainer: "simpleTree-nodeContainer",
    selected: "simpleTree-selected",
    toggle: "simpleTree-toggle",
  },
};

console.log("made it this far");
async function loadSimpleBookmarks() {
  console.log("Loading AI bookmarks...");
  const data = await loadAiBookmarks();
  console.log("AI bookmarks loaded successfully:", data);
  $("#simpleTree").simpleTree(_defaults, data);
  console.log(data);
}

async function loadAiBookmarks() {
  try {
    const response = await fetch("public/ai_bookmarks.json");
    if (!response.ok) {
      throw new Error(
        `Failed to load AI bookmarks: ${response.status} ${response.statusText}`
      );
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error loading AI bookmarks:", error);
    return {};
  }
}

// Only execute when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  loadSimpleBookmarks();
});
