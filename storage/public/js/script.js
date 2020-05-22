function dynamicSearch() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("countrySearch");
    filter = input.value.toUpperCase();
    tr = document.getElementsByClassName('table-row');
    console.log(tr)
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
    }
}