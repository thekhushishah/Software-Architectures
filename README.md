# Software-Architectures
CSCI 578 - USC

Version Change Visualisation


This project provides an overview of the changes between two versions in a system. This helps us identify distinctions in the clusters, dependencies and most dependent components between two versions of a system. This can also be used to identify cyclic dependencies and components that are tightly coupled. The sensitivity points along with the components that could be impacted by this can be seen in the visualization.


Prerequisites


Install python


This can also be used to run a simple python server to view the html page


Write the following command in terminal:
python -m SimpleHTTPServer
	

Running the code


The input to this project are the cluster.rsf and deps.rsf files from the RELAX recovery method.
The file config.json contains the configuration required by the python code to produce the intermediate json files for the front end.
Based on the stats required, changes can be made in config.json


{
"cluster-files":["chukwa-0.1.2_relax_clusters.rsf","chukwa-0.2.0_relax_clusters.rsf"],
"deps-files":["chukwa-0.1.2_deps.rsf","chukwa-0.2.0_deps.rsf"]
}
	

Run the python code. 


python FinalProject.py
	

This generates the JSON output files for the visualization:
compare.json
matrix.json
most_important_class.json


If the python(or any other) server is up and running. By opening the following url, on the browser, we can see the visualization:


http://localhost:8000/FinalProject/integrated.html
	

File Description


Configuration file:
* config.json : The user can specify the input files to the python program.
Python file:
* FinalProject.py : This contains the code that processes the four rsf files (deps.rsf and cluster.rsf for both versions) to generate the intermediate JSON output files required by the HTML visualisation
HTML files:
* matrix.html : This contains the necessary html and javascript code to visualise the dependency structure matrix. On clicking individual numbers in the cell of the matrix, we get detailed dependency information 
* highcharts.html : This contains the necessary bar graph information to display the sensitivity points in the system.
* circle.html : This contains the clusters along with the added, removed and unchanged sections within each to visualise an overview about the system
Intermediate Output files:
* compare.json - Data about how components are grouped into clusters; as an input to circle.html
* matrix.json - Data regarding how the clusters are depending on each other and within them, the corresponding files that are dependent; as an input to matrix.html
* bar_graph.json - Data regarding the crucial components along with the components that depend on them; as an input to highcharts.html


Libraries used


* Bootstrap(https://getbootstrap.com/)
* Highcharts(https://www.highcharts.com/)
* D3(https://d3js.org/)
* JQuery(http://jquery.com/)
