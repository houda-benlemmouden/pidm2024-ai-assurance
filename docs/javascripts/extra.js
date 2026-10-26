function wrapWideTables() {
  document.querySelectorAll(".md-typeset table").forEach((table) => {
    if (table.parentElement?.classList.contains("table-scroll")) {
      return;
    }

    const wrapper = document.createElement("div");
    wrapper.className = "table-scroll";
    wrapper.setAttribute("role", "region");
    wrapper.setAttribute("aria-label", "Scrollable data table");
    wrapper.setAttribute("tabindex", "0");

    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
  });
}

document$.subscribe(() => {
  wrapWideTables();
});