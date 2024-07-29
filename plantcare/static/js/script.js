document.addEventListener('DOMContentLoaded', function() {
    // Initialize sidebar
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // Initialize dropdown
    var dropdowns = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(dropdowns);

    // Initialize selectors
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);
    
    // Initialize collapsibles
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);
});