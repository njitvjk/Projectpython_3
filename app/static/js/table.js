$(document).ready(function () {
      $('#data').DataTable({
        columns: [
          {data: 'value[0]'},
          {data: 'value[1]', searchable: false},
          {data: 'value[2]', orderable: false, searchable: false}, {data: 'value[3]', orderable: false, searchable: true}],


      });
    });