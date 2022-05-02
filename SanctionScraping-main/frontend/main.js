$(document).ready(function () {
  // Setup - add a text input to each footer cell
  $("#sanctions thead tr")
    .clone(true)
    .addClass("filters")
    .appendTo("#sanctions thead");

  var table = $("#sanctions").DataTable({
    orderCellsTop: true,
    fixedHeader: true,
    initComplete: function () {
      var api = this.api();

      // For each column
      api
        .columns()
        .eq(0)
        .each(function (colIdx) {
          // Set the header cell to contain the input element
          var cell = $(".filters th").eq(
            $(api.column(colIdx).header()).index()
          );
          var title = $(cell).text();
          $(cell).html('<input type="text" placeholder="' + title + '" />');

          // On every keypress in this input
          $(
            "input",
            $(".filters th").eq($(api.column(colIdx).header()).index())
          )
            .off("keyup change")
            .on("keyup change", function (e) {
              e.stopPropagation();

              // Get the search value
              $(this).attr("title", $(this).val());
              var regexr = "({search})"; //$(this).parents('th').find('select').val();

              var cursorPosition = this.selectionStart;
              // Search the column for that value
              api
                .column(colIdx)
                .search(
                  this.value != ""
                    ? regexr.replace("{search}", "(((" + this.value + ")))")
                    : "",
                  this.value != "",
                  this.value == ""
                )
                .draw();

              $(this)
                .focus()[0]
                .setSelectionRange(cursorPosition, cursorPosition);
            });
        });
    },
    ajax: {
      url: "https://sanctions-server.herokuapp.com/sanctions",
      type: "GET",
      dataSrc: "",
    },
    columns: [
      { data: "Source", searchable: true },
      { data: "Name", searchable: true },
      { data: "Address", searchable: true },
      { data: "Sanction Type", searchable: true },
      { data: "Other Name", searchable: false },
      { data: "Country", searchable: true },
      { data: "Eligibility Period", searchable: false },
      { data: "Grounds", searchable: true },
    ],
    language: {
      emptyTable: "Your search has not returned any result",
    },
    info: false,
  });
});
