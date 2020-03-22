object.onkeyup =function filtrarNombres() {

var input, filter, table, tr, td, i, txtValue, txtValue_2;
input = document.getElementById("filtro");
filter = input.value.toUpperCase();
table = document.getElementById("tablaAlumnos");
tr = table.getElementsByTagName("tr");

for (i = 0; i < tr.length; i++) {
  td = tr[i].getElementsByTagName("td")[0];
  td_2 = tr[i].getElementsByTagName("td")[1];
  if (td) {
    txtValue = td.textContent || td.innerText;
    txtValue_2 = td_2.textContent || td_2.innerText;
    txtValue_sum=txtValue+" "+txtValue_2;
    if (txtValue.toUpperCase().includes(filter) || txtValue_2.toUpperCase().includes(filter) || txtValue_3.toUpperCase().includes(filter) )
      {
        tr[i].style.display = "";
      }
    else
      {
        tr[i].style.display = "none";
      }
    }
  }
}
