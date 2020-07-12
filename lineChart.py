import bpy

class LineChart(object):

    bevel_obj_size = (0.1, 0.1, 0.1)
    def add_bevel_obj(self, curve_obj, description):
        '''Adds bevel object to existing curve'''
        bpy.ops.mesh.primitive_plane_add()
        bevel_obj = bpy.context.active_object
        bevel_obj.name = description+"line_chart_plane"
        bevel_obj.scale = self.bevel_obj_size

        bpy.ops.object.convert(target='CURVE')
        curve_obj.data.bevel_object = bevel_obj
        return bevel_obj

    def select_curve_obj(self, curve_obj):
        curve_obj.select_set(True)
        bpy.context.view_layer.objects.active = curve_obj

    def plotdata(self, x , y , min_x, max_x, min_y, max_y, start_keyframe, data, description, sizes ):
        self.bevel_obj_size=sizes
        print('plotdata')
        bpy.ops.object.select_all(action='DESELECT')
        if bpy.data.objects.get(description+'line_chart_curve') is not None:
            try:
                bpy.data.objects[description+'line_chart_curve'].select_set(True)
            except:
                print('exception')
        if bpy.data.objects.get(description+"line_chart_plane") is not None:
            try:
                bpy.data.objects[description+"line_chart_plane"].select_set(True)
            except:
                print('exception')
        bpy.ops.object.delete()

        verts=[(x+i/10, y+i/10, 0.0) for i in range(0,100)]
        edges = [[i - 1, i] for i in range(1, len(verts))]

        m = bpy.data.meshes.new('line_mesh')
        curve_obj = bpy.data.objects.new(description+'line_chart_curve', m)
        #curve_obj.data.twist_mode = 'TANGENT'
        bpy.context.scene.collection.objects.link(curve_obj)
        #curve_obj.parent = self.container_object
        m.from_pydata(verts, edges, [])
        m.update()

        self.select_curve_obj(curve_obj)
        #if self.bevel_edges:
        #    self.bevel_curve_obj()

        bpy.ops.object.convert(target='CURVE')
        self.add_bevel_obj(curve_obj,description)
        points=curve_obj.data.splines[0].points
        #tmp=[data[i] for i in range(0:100)]
        for i in range(0,len(data)-100):
            if(i%100==0):
                print(str(i))
            for j in range(0,100):
                val=(data[i+j]-min(data))/(max(data)-min(data))
                points[j].co[1]=y+val*max_y
                points[j].keyframe_insert(data_path="co", frame = start_keyframe+i)
