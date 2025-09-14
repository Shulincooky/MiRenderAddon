# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Minecraft Render Engine",
    "author": "Shulin&Baigave",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Render",
}
import bpy
from bpy.types import RenderEngine


class MinecraftRender(RenderEngine):
    bl_idname = "MINECRAFT"
    bl_label = "Minecraft"
    bl_use_preview = True

    def render(self, depsgraph):
        """Produce a solid‑black image so the engine appears to work."""
        width = self.resolution_x
        height = self.resolution_y

        # Create an empty result tile covering the whole frame
        result = self.begin_result(0, 0, width, height)
        layer = result.layers[0]

        # Set every pixel to opaque black (R, G, B, A)
        layer.rect = [0.0, 0.0, 0.0, 1.0] * (width * height)

        # Hand the buffer back to Blender
        self.end_result(result)

    # Optional stubs so Blender doesn’t spam the console
    def view_update(self, context, depsgraph):
        pass

    def view_draw(self, context, depsgraph):
        pass


def register():
    bpy.utils.register_class(MinecraftRender)


def unregister():
    bpy.utils.unregister_class(MinecraftRender)


if __name__ == "__main__":
    register()
