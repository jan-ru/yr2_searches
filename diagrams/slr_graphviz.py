from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("Grouped Workers", show=False, direction="TB"):
    EC2("lb") >> [EC2("worker1"), EC2("worker2")]
