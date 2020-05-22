$(document).ready(function () {
  var defaultData = [];
  var labels = [];
  $.ajax({
    method: "GET",
    url: "ajax/chartData",
    success: function (data) {
      labels = data.labels;
      defaultData = data.default;
      var ctx = document.getElementById("myChart").getContext("2d");
      var myChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: labels,
          datasets: [
            {
              label: "# of Votes",
              data: defaultData,
            },
          ],
        },
      });
    },
    error: function (error_data) {
      console.log("error");
      console.log(error_data);
    },
  });
});
