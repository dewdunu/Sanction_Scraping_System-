$(document).ready(function() {

    $('#sanctions tfoot th').each( function () {
        let title = $(this).text();
        $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
    } );

    let table = $('#sanctions').DataTable({
        initComplete: function () {
            // Apply the search
            this.api().columns().every( function () {
                let that = this;
                $( 'input', this.footer() ).on( 'keyup change clear', function () {
                    if ( that.search() !== this.value ) {
                        that
                            .search( this.value )
                            .draw();
                    }
                } );
            } );
        },
        ajax: {
            url : "https://sanctions-server.herokuapp.com/sanctions",
            type : "GET",
            dataSrc : ""
        },
        columns: [
            { data : "Source", searchable : true},
            { data : "Name" , searchable : true},
            { data : "Address", searchable : true},
            { data : "Sanction Type", searchable : true},
            { data : "Other Name", searchable : false},
            { data : "Country", searchable : true},
            { data : "Eligibility Period", searchable : false},
            { data : "Grounds", searchable : true}
        ],
        language : {
            emptyTable: "Your search has not returned any result"
        },
        info: false
    } );
});