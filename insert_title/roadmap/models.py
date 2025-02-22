from django.db import models


class Roadmap(models.Model):
    road_map_name = models.CharField(max_length=250)
    node_name=models.CharField(max_length=250)
    nested_nodes = models.CharField(default=0,max_length=250)
    finished_node=models.BooleanField(default=False)


    def __str__(self):
        return self.road_map_name