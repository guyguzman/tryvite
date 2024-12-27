async function loadBookmarks() {
  const response = await fetch("ai_bookmarks.json");
  const bookmarks = await response.json();
  return bookmarks;
}

function sortByName(items) {
  return items.sort((a, b) => a.name.localeCompare(b.name));
}

function createFolderElement(folder) {
  const folderDiv = document.createElement("div");
  folderDiv.className = "folder";

  const header = document.createElement("div");
  header.className = "folder-header";

  const button = document.createElement("button");
  button.className = "expand-button";
  button.textContent = "+";

  const name = document.createElement("span");
  name.className = "folder-name";
  name.textContent = folder.name;

  const content = document.createElement("div");
  content.className = "folder-content";

  if (folder.children) {
    const links = document.createElement("div");
    links.className = "bookmark-grid";
    sortByName(folder.children).forEach((child) => {
      if (child.type === "url") {
        links.appendChild(createBookmarkElement(child));
      }
    });
    content.appendChild(links);
  }

  header.appendChild(button);
  header.appendChild(name);
  folderDiv.appendChild(header);
  folderDiv.appendChild(content);

  header.addEventListener("click", () => {
    content.classList.toggle("expanded");
    button.textContent = content.classList.contains("expanded") ? "-" : "+";
  });

  return folderDiv;
}

function createBookmarkElement(bookmark) {
  const link = document.createElement("a");
  link.href = bookmark.url;
  link.className = "bookmark-link";
  link.textContent = bookmark.name + ", " + bookmark.id;
  link.target = "_blank";
  return link;
}

async function init() {
  const bookmarks = await loadBookmarks();
  const foldersSection = document.getElementById("folders-section");
  const urlsSection = document.getElementById("urls-section");

  // Render folders
  const folders = bookmarks.filter((b) => b.type === "folder");
  sortByName(folders).forEach((folder) => {
    foldersSection.appendChild(createFolderElement(folder));
  });

  // Render top-level URLs
  const urls = bookmarks.filter((b) => b.type === "url");
  const urlsGrid = document.createElement("div");
  urlsGrid.className = "bookmark-grid";
  sortByName(urls).forEach((bookmark) => {
    urlsGrid.appendChild(createBookmarkElement(bookmark));
  });
  urlsSection.appendChild(urlsGrid);
}

init();
