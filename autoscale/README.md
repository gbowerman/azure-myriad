### Template to add autoscale rules to an existing VM scale set

If you have an existing Azure VM scale set which does not have autoscale rules set up, you can deploy this template into the same resource group, and pass in the scale set name as a parameter. It will set up autoscale rules based on CPU utilization. 

To do: This template could be made more versatile by making the autoscale settings (like the metric names and threshold percentages) into parameters. For now, edit the template at deployment time to change the threshold values.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fautoscale%2Faddautoscale.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fgbowerman%2Fazure-myriad%2Fmaster%2Fautoscale%2Faddautoscale.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>
