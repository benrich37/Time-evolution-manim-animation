import numpy as np
from manimlib import Scene, Tex, BLUE, RED, WHITE, UP, ThreeDAxes, OUT, LEFT, \
    RIGHT, ValueTracker, Vector


class AxisVector(Scene):
    None
    # Will be parent for smoothie and spiky vector

# class SmoothieVector(Scene):
#     n = 2
#     ax_range = 1
#     origins = [None] * n
#     axes = [None] * n
#     vec = np.empty((n,), dtype=complex)
#     vec_track = [[None]*3]*n
#     vec_draw = [[None]*3]*n
#     brackets = []
#     bracketL = Tex("\\Bigg[")
#     bracketR = Tex("\\Bigg]")
#     colorRe = BLUE
#     colorIm = RED
#     colorMod = WHITE
#
#     def __init__(self,n,ax_range,vec):
#         self.n = n
#         self.ax_range = ax_range
#         self.vec = vec
#         self.norm_vector()
#         self.origins = self.init_empty_list_of_lists(self.n,0)
#         self.axes = self.init_empty_list_of_lists(self.n,0)
#         self.vec_track = self.init_empty_list_of_lists(self.n,3)
#         self.vec_draw = self.init_empty_list_of_lists(self.n,3)
#
#         self.init_origins()
#         self.init_trackers()
#         self.set_trackers()
#         self.init_axes()
#         self.init_draw_vec()
#         self.init_draw_vec_updaters()
#         self.init_brackets()
#
#
#
#
#     ### INTERNAL METHODS
#     ## INIT PRIMARY METHODS
#     # (methods directly called in init function)
#     def norm_vector(self):
#         norms = np.linalg.norm(self.vec)
#         self.vec = self.vec / norms
#
#     def init_empty_list_of_lists(self,width,depth):
#         out = self.init_list_of_list(width)
#         for i in np.arange(width):
#             self.expand_empty_list(out[i],depth)
#         return out
#
#     def init_origins(self):
#         for i in np.arange(self.n):
#             self.origins[i] = (2*i - (self.n/2)) * UP * 1.5 * self.ax_range
#
#     def init_trackers(self):
#         for i in np.arange(self.n):
#             self.init_some_trackers(i)
#
#     def set_trackers(self):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.set_tracker(i,j)
#
#     def init_axes(self):
#         for i in np.arange(self.n):
#             self.axes[i] = ThreeDAxes(
#                 x_range=[-self.ax_range, self.ax_range, 1],
#                 y_range=[-self.ax_range, self.ax_range, 1],
#                 z_range=[0, self.ax_range, 1],
#                 x_length=self.ax_range,
#                 y_length=self.ax_range,
#                 z_length=self.ax_range,
#             ).move_to(self.origins[i]).shift(OUT * self.ax_range / 2)
#
#     def init_draw_vec(self):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.vec_draw[i][j] = self.make_draw_vec(i,j)
#
#     def init_draw_vec_updaters(self):
#         for i in np.arange(self.n):
#             for j in np.arange(2):
#                 self.give_updater(self.vec_draw[i][j],i,j)
#
#     def init_brackets(self):
#         self.brackets = []
#         self.bracketL = Tex("\\Bigg[")
#         self.bracketR = Tex("\\Bigg]")
#         self.bracketL.scale((3 * self.n * self.ax_range) / self.bracketL.get_height()).shift(LEFT * self.ax_range)
#         self.bracketR.scale((3 * self.n * self.ax_range) / self.bracketR.get_height()).shift(RIGHT * self.ax_range)
#         self.brackets.append(self.bracketL)
#         self.brackets.append(self.bracketR)
#
#
#     ## INIT SECONDARY METHODS
#     # (methods called in primary methods)
#     def init_list_of_list(self,width):
#         out = []
#         for i in np.arange(width):
#             out.append([])
#         return out
#     def expand_empty_list(self,list,depth):
#         for j in np.arange(depth):
#             list.append(None)
#
#     def init_some_trackers(self,i):
#         for j in np.arange(3):
#             self.vec_track[i][j] = self.make_tracker()
#     def make_tracker(self):
#         return ValueTracker()
#
#     def set_tracker(self,i,j):
#         if j == 0:
#             self.vec_track[i][j].set_value(np.real(self.vec[i]))
#         if j == 1:
#             self.vec_track[i][j].set_value(np.imag(self.vec[i]))
#         if j == 2:
#             self.vec_track[i][j].set_value(abs(self.vec[i]))
#
#     def make_draw_vec(self,i,j):
#         output_vec = None
#         vec_color, vec_dir = self.get_draw_vec_perams(j)
#
#         output_vec = Vector().set_color(vec_color)
#         output_vec.set_points_by_ends(self.origins[i],
#                                       self.origins[i] + self.vec_track[i][j].get_value() * vec_dir)
#         return output_vec
#     def get_draw_vec_perams(self,j):
#         vec_color = None
#         vec_dir = None
#         if j == 0:
#             vec_color = self.colorRe
#             vec_dir = RIGHT
#         if j == 1:
#             vec_color = self.colorIm
#             vec_dir = UP
#         if j == 2:
#             vec_color = self.colorMod
#             vec_dir = OUT
#         return vec_color, vec_dir
#
#     def give_updater(self,obj,i,j):
#         vec_dir = None
#         if j == 0:
#             obj.add_updater(
#                 lambda v: v.set_points_by_ends(self.origins[i],
#                                                self.origins[i] +
#                                                (self.vec_track[i][0].get_value() * RIGHT) +
#                                                (self.vec_track[i][1].get_value() * UP)
#                                                ))
#         if j == 1:
#             obj.add_updater(
#                 lambda v: v.set_points_by_ends(self.origins[i],
#                                                self.origins[i] +
#                                                (self.vec_track[i][2].get_value() * OUT)
#                                                ))
#
#
#     ## EXTERNAL SECONDARY METHODS
#     # (methods called for external methods)
#     def tracker_set_val(self,i):
#         args = []
#         args.append(self.vec_track[i][0].animate.set_value(np.real(self.vec[i])))
#         args.append(self.vec_track[i][1].animate.set_value(np.imag(self.vec[i])))
#         args.append(self.vec_track[i][2].animate.set_value(abs(self.vec[i])))
#         return args
#
#     def animate_shift_origins(self, vector):
#         for i in np.arange(self.n):
#             self.origins[i] = self.origins[i] + vector
#
#     def animate_shift_vec_draws(self, vector):
#         args = []
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 args.append(self.vec_draw[i][j].animate.shift(vector))
#         return args
#
#     def animate_shift_brackets(self, vector):
#         args = []
#         for i in np.arange(len(self.brackets)):
#             args.append(self.brackets[i].animate.shift(vector))
#         return args
#
#     def animate_shift_axes(self, vector):
#         args = []
#         for i in np.arange(len(self.axes)):
#             args.append(self.axes[i].animate.shift(vector))
#         return args
#
#     def shift_origins(self, vector):
#         for i in np.arange(self.n):
#             self.origins[i] = self.origins[i] + vector
#
#     def shift_vec_draws(self, vector):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.vec_draw[i][j].shift(vector)
#
#     def shift_brackets(self, vector):
#         for i in np.arange(len(self.brackets)):
#             self.brackets[i].shift(vector)
#
#
#
#     ### EXTERNAL METHODS
#     # (methods that you should be using in your scene)
#     def add_all(self):
#         args = []
#         for i in np.arange(len(self.axes)):
#             args.append(self.axes[i])
#         for j in np.arange(len(self.brackets)):
#             args.append(self.brackets[j])
#         for k in np.arange(len(self.give_vec())):
#             args.append(self.give_vec()[k])
#         return args
#
#     def tracker_set_vals(self):
#         # use like "self.play(*spiky.tracker_set_vals())"
#         args = []
#         for i in np.arange(self.n):
#             temp_args = []
#             temp_args = self.tracker_set_val(i)
#             args.append(temp_args[0])
#             args.append(temp_args[1])
#             args.append(temp_args[2])
#         return args
#
#     def give_vec(self):
#         args = []
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 args.append(self.vec_draw[i][j])
#         return args
#
#     def animate_shift_mobjects(self, vector):
#         args = []
#         self.animate_shift_origins(vector)
#         vec_args = self.animate_shift_vec_draws(vector)
#         brack_args = self.animate_shift_brackets(vector)
#         ax_args = self.animate_shift_axes(vector)
#         for v in np.arange(len(vec_args)):
#             args.append(vec_args[v])
#         for b in np.arange(len(brack_args)):
#             args.append(brack_args[b])
#         for a in np.arange(len(ax_args)):
#             args.append(ax_args[a])
#         return args
#     # # Commented out because I don't want to finish the helper functions
#     # def shift_mobjects(self, vector):
#     #     self.shift_origins(vector)
#     #     self.shift_vec_draws(vector)
#     #     self.shift_brackets(vector)
#
# class SpikyVector(Scene):
#     cirhuh = False
#     n = 2
#     ax_range = 1
#     origins = [None] * n
#     axes = [None] * n
#     vec = np.empty((n,), dtype=complex)
#     vec_track = [[None]*3]*n
#     vec_draw = [[None]*3]*n
#     brackets = []
#     bracketL = Tex("\\Bigg[")
#     bracketR = Tex("\\Bigg]")
#     colorRe = BLUE
#     colorIm = RED
#     colorMod = WHITE
#
#     def __init__(self,cirhuh,n,ax_range,vec):
#         self.cirhuh = cirhuh
#         self.n = n
#         self.ax_range = ax_range
#         self.vec = vec
#         self.norm_vector()
#         self.origins = self.init_empty_list_of_lists(self.n,0)
#         self.axes = self.init_empty_list_of_lists(self.n,0)
#         self.vec_track = self.init_empty_list_of_lists(self.n,3)
#         self.vec_draw = self.init_empty_list_of_lists(self.n,3)
#
#         self.init_origins()
#         self.init_trackers()
#         self.set_trackers()
#         self.init_axes()
#         self.init_draw_vec()
#         self.init_draw_vec_updaters()
#         self.init_brackets()
#
#
#
#
#     ### INTERNAL METHODS
#     ## INIT PRIMARY METHODS
#     # (methods directly called in init function)
#     def norm_vector(self):
#         norms = np.linalg.norm(self.vec)
#         self.vec = self.vec / norms
#
#     def init_empty_list_of_lists(self,width,depth):
#         out = self.init_list_of_list(width)
#         for i in np.arange(width):
#             self.expand_empty_list(out[i],depth)
#         return out
#
#     def init_origins(self):
#         for i in np.arange(self.n):
#             self.origins[i] = (2*i - (self.n/2)) * UP * 1.5 * self.ax_range
#
#     def init_trackers(self):
#         for i in np.arange(self.n):
#             self.init_some_trackers(i)
#
#     def set_trackers(self):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.set_tracker(i,j)
#
#     def init_axes(self):
#         for i in np.arange(self.n):
#             self.axes[i] = ThreeDAxes(
#                 x_range=[-self.ax_range, self.ax_range, 1],
#                 y_range=[-self.ax_range, self.ax_range, 1],
#                 z_range=[0, self.ax_range, 1],
#                 x_length=self.ax_range,
#                 y_length=self.ax_range,
#                 z_length=self.ax_range,
#             ).move_to(self.origins[i]).shift(OUT * self.ax_range / 2)
#
#     def init_draw_vec(self):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.vec_draw[i][j] = self.make_draw_vec(i,j)
#
#     def init_draw_vec_updaters(self):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.give_updater(self.vec_draw[i][j],i,j)
#
#     def init_brackets(self):
#         self.brackets = []
#         self.bracketL = Tex("\\Bigg[")
#         self.bracketR = Tex("\\Bigg]")
#         self.bracketL.scale((3 * self.n * self.ax_range) / self.bracketL.get_height()).shift(LEFT * self.ax_range).shift(UP)
#         self.bracketR.scale((3 * self.n * self.ax_range) / self.bracketR.get_height()).shift(RIGHT * self.ax_range).shift(UP)
#         self.brackets.append(self.bracketL)
#         self.brackets.append(self.bracketR)
#
#
#     ## INIT SECONDARY METHODS
#     # (methods called in primary methods)
#     def init_list_of_list(self,width):
#         out = []
#         for i in np.arange(width):
#             out.append([])
#         return out
#     def expand_empty_list(self,list,depth):
#         for j in np.arange(depth):
#             list.append(None)
#
#     def init_some_trackers(self,i):
#         for j in np.arange(3):
#             self.vec_track[i][j] = self.make_tracker()
#     def make_tracker(self):
#         return ValueTracker()
#
#     def set_tracker(self,i,j):
#         if j == 0:
#             self.vec_track[i][j].set_value(np.real(self.vec[i]))
#         if j == 1:
#             self.vec_track[i][j].set_value(np.imag(self.vec[i]))
#         if j == 2:
#             self.vec_track[i][j].set_value(abs(self.vec[i]))
#
#     def make_draw_vec(self,i,j):
#         output_vec = None
#         vec_color, vec_dir = self.get_draw_vec_perams(j)
#
#         output_vec = Vector().set_color(vec_color)
#         output_vec.set_points_by_ends(self.origins[i],
#                                       self.origins[i] + self.vec_track[i][j].get_value() * vec_dir)
#         return output_vec
#     def get_draw_vec_perams(self,j):
#         vec_color = None
#         vec_dir = None
#         if j == 0:
#             vec_color = self.colorRe
#             vec_dir = RIGHT
#         if j == 1:
#             vec_color = self.colorIm
#             vec_dir = UP
#         if j == 2:
#             vec_color = self.colorMod
#             vec_dir = OUT
#         return vec_color, vec_dir
#
#     def give_updater(self,obj,i,j):
#         vec_dir = None
#         if j == 0:
#             vec_color = self.colorRe
#             vec_dir = RIGHT
#         if j == 1:
#             vec_color = self.colorIm
#             vec_dir = UP
#         if j == 2:
#             vec_color = self.colorMod
#             vec_dir = OUT
#         obj.add_updater(
#             lambda v: v.set_points_by_ends(self.origins[i],
#                                            self.origins[i] + self.vec_track[i][j].get_value() * vec_dir))
#
#     ## EXTERNAL SECONDARY METHODS
#     # (methods called for external methods)
#     def tracker_set_val(self,i):
#         args = []
#         args.append(self.vec_track[i][0].animate.set_value(np.real(self.vec[i])))
#         args.append(self.vec_track[i][1].animate.set_value(np.imag(self.vec[i])))
#         args.append(self.vec_track[i][2].animate.set_value(abs(self.vec[i])))
#         return args
#
#     def animate_shift_origins(self, vector):
#         for i in np.arange(self.n):
#             self.origins[i] = self.origins[i] + vector
#
#     def animate_shift_vec_draws(self, vector):
#         args = []
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 args.append(self.vec_draw[i][j].animate.shift(vector))
#         return args
#
#     def animate_shift_brackets(self, vector):
#         args = []
#         for i in np.arange(len(self.brackets)):
#             args.append(self.brackets[i].animate.shift(vector))
#         return args
#
#     def animate_shift_axes(self, vector):
#         args = []
#         for i in np.arange(len(self.axes)):
#             args.append(self.axes[i].animate.shift(vector))
#         return args
#
#     def shift_origins(self, vector):
#         for i in np.arange(self.n):
#             self.origins[i] = self.origins[i] + vector
#
#     def shift_vec_draws(self, vector):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.vec_draw[i][j].shift(vector)
#
#     def shift_brackets(self, vector):
#         for i in np.arange(len(self.brackets)):
#             self.brackets[i].shift(vector)
#
#
#
#     ### EXTERNAL METHODS
#     # (methods that you should be using in your scene)
#     def add_all(self):
#         args = []
#         for i in np.arange(len(self.axes)):
#             args.append(self.axes[i])
#         for j in np.arange(len(self.brackets)):
#             args.append(self.brackets[j])
#         for k in np.arange(len(self.give_vec())):
#             args.append(self.give_vec()[k])
#         return args
#
#     def tracker_set_vals(self):
#         # use like "self.play(*spiky.tracker_set_vals())"
#         args = []
#         for i in np.arange(self.n):
#             temp_args = []
#             temp_args = self.tracker_set_val(i)
#             args.append(temp_args[0])
#             args.append(temp_args[1])
#             args.append(temp_args[2])
#         return args
#
#     def give_vec(self):
#         args = []
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 args.append(self.vec_draw[i][j])
#         return args
#
#     def animate_shift_mobjects(self, vector):
#         args = []
#         self.animate_shift_origins(vector)
#         vec_args = self.animate_shift_vec_draws(vector)
#         brack_args = self.animate_shift_brackets(vector)
#         ax_args = self.animate_shift_axes(vector)
#         for v in np.arange(len(vec_args)):
#             args.append(vec_args[v])
#         for b in np.arange(len(brack_args)):
#             args.append(brack_args[b])
#         for a in np.arange(len(ax_args)):
#             args.append(ax_args[a])
#         return args
#     # # Commented out because I don't want to finish the helper functions
#     # def shift_mobjects(self, vector):
#     #     self.shift_origins(vector)
#     #     self.shift_vec_draws(vector)
#     #     self.shift_brackets(vector)
#
#
# class SmoothieVectorFromMethods(Scene):
#     n = 2
#     ax_range = 1
#     origins = [None] * n
#     axes = [None] * n
#     vec = np.empty((n,), dtype=complex)
#     vec_track = [[None]*3]*n
#     vec_draw = [[None]*3]*n
#     brackets = []
#     bracketL = Tex("\\Bigg[")
#     bracketR = Tex("\\Bigg]")
#     colorRe = BLUE
#     colorIm = RED
#     colorMod = WHITE
#
#     def __init__(self,n,ax_range,vec):
#         self.n = n
#         self.ax_range = ax_range
#         self.vec = vec
#         self.norm_vector()
#         self.origins = self.init_empty_list_of_lists(self.n,0)
#         self.axes = self.init_empty_list_of_lists(self.n,0)
#         self.vec_track = self.init_empty_list_of_lists(self.n,3)
#         self.vec_draw = self.init_empty_list_of_lists(self.n,3)
#
#         self.init_origins()
#         self.init_trackers()
#         self.set_trackers()
#         self.init_axes()
#         self.init_draw_vec()
#         self.init_draw_vec_updaters()
#         self.init_brackets()
#
#
#
#
#     ### INTERNAL METHODS
#     ## INIT PRIMARY METHODS
#     # (methods directly called in init function)
#     def norm_vector(self):
#         norms = np.linalg.norm(self.vec)
#         self.vec = self.vec / norms
#
#     def init_empty_list_of_lists(self,width,depth):
#         out = self.init_list_of_list(width)
#         for i in np.arange(width):
#             self.expand_empty_list(out[i],depth)
#         return out
#
#     def init_origins(self):
#         for i in np.arange(self.n):
#             self.origins[i] = (2*i - (self.n/2)) * UP * 1.5 * self.ax_range
#
#     def init_trackers(self):
#         for i in np.arange(self.n):
#             self.init_some_trackers(i)
#
#     def set_trackers(self):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.set_tracker(i,j)
#
#     def init_axes(self):
#         for i in np.arange(self.n):
#             self.axes[i] = ThreeDAxes(
#                 x_range=[-self.ax_range, self.ax_range, 1],
#                 y_range=[-self.ax_range, self.ax_range, 1],
#                 z_range=[0, self.ax_range, 1],
#                 x_length=self.ax_range,
#                 y_length=self.ax_range,
#                 z_length=self.ax_range,
#             ).move_to(self.origins[i]).shift(OUT * self.ax_range / 2)
#
#     def init_draw_vec(self):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.vec_draw[i][j] = self.make_draw_vec(i,j)
#
#     def init_draw_vec_updaters(self):
#         for i in np.arange(self.n):
#             for j in np.arange(2):
#                 self.give_updater(self.vec_draw[i][j],i,j)
#
#     def init_brackets(self):
#         self.brackets = []
#         self.bracketL = Tex("\\Bigg[")
#         self.bracketR = Tex("\\Bigg]")
#         self.bracketL.scale((3 * self.n * self.ax_range) / self.bracketL.get_height()).shift(LEFT * self.ax_range)
#         self.bracketR.scale((3 * self.n * self.ax_range) / self.bracketR.get_height()).shift(RIGHT * self.ax_range)
#         self.brackets.append(self.bracketL)
#         self.brackets.append(self.bracketR)
#
#
#     ## INIT SECONDARY METHODS
#     # (methods called in primary methods)
#     def init_list_of_list(self,width):
#         out = []
#         for i in np.arange(width):
#             out.append([])
#         return out
#     def expand_empty_list(self,list,depth):
#         for j in np.arange(depth):
#             list.append(None)
#
#     def init_some_trackers(self,i):
#         for j in np.arange(3):
#             self.vec_track[i][j] = self.make_tracker()
#     def make_tracker(self):
#         return ValueTracker()
#
#     def set_tracker(self,i,j):
#         if j == 0:
#             self.vec_track[i][j].set_value(np.real(self.vec[i]))
#         if j == 1:
#             self.vec_track[i][j].set_value(np.imag(self.vec[i]))
#         if j == 2:
#             self.vec_track[i][j].set_value(abs(self.vec[i]))
#
#     def make_draw_vec(self,i,j):
#         output_vec = None
#         vec_color, vec_dir = self.get_draw_vec_perams(j)
#
#         output_vec = Vector().set_color(vec_color)
#         output_vec.set_points_by_ends(self.origins[i],
#                                       self.origins[i] + self.vec_track[i][j].get_value() * vec_dir)
#         return output_vec
#     def get_draw_vec_perams(self,j):
#         vec_color = None
#         vec_dir = None
#         if j == 0:
#             vec_color = self.colorRe
#             vec_dir = RIGHT
#         if j == 1:
#             vec_color = self.colorIm
#             vec_dir = UP
#         if j == 2:
#             vec_color = self.colorMod
#             vec_dir = OUT
#         return vec_color, vec_dir
#
#     def give_updater(self,obj,i,j):
#         vec_dir = None
#         if j == 0:
#             obj.add_updater(
#                 lambda v: v.set_points_by_ends(self.origins[i],
#                                                self.origins[i] +
#                                                (self.vec_track[i][0].get_value() * RIGHT) +
#                                                (self.vec_track[i][1].get_value() * UP)
#                                                ))
#         if j == 1:
#             obj.add_updater(
#                 lambda v: v.set_points_by_ends(self.origins[i],
#                                                self.origins[i] +
#                                                (self.vec_track[i][2].get_value() * OUT)
#                                                ))
#
#
#     ## EXTERNAL SECONDARY METHODS
#     # (methods called for external methods)
#     def tracker_set_val(self,i):
#         args = []
#         args.append(self.vec_track[i][0].animate.set_value(np.real(self.vec[i])))
#         args.append(self.vec_track[i][1].animate.set_value(np.imag(self.vec[i])))
#         args.append(self.vec_track[i][2].animate.set_value(abs(self.vec[i])))
#         return args
#
#     def animate_shift_origins(self, vector):
#         for i in np.arange(self.n):
#             self.origins[i] = self.origins[i] + vector
#
#     def animate_shift_vec_draws(self, vector):
#         args = []
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 args.append(self.vec_draw[i][j].animate.shift(vector))
#         return args
#
#     def animate_shift_brackets(self, vector):
#         args = []
#         for i in np.arange(len(self.brackets)):
#             args.append(self.brackets[i].animate.shift(vector))
#         return args
#
#     def animate_shift_axes(self, vector):
#         args = []
#         for i in np.arange(len(self.axes)):
#             args.append(self.axes[i].animate.shift(vector))
#         return args
#
#     def shift_origins(self, vector):
#         for i in np.arange(self.n):
#             self.origins[i] = self.origins[i] + vector
#
#     def shift_vec_draws(self, vector):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.vec_draw[i][j].shift(vector)
#
#     def shift_brackets(self, vector):
#         for i in np.arange(len(self.brackets)):
#             self.brackets[i].shift(vector)
#
#
#
#     ### EXTERNAL METHODS
#     # (methods that you should be using in your scene)
#     def add_all(self):
#         args = []
#         for i in np.arange(len(self.axes)):
#             args.append(self.axes[i])
#         for j in np.arange(len(self.brackets)):
#             args.append(self.brackets[j])
#         for k in np.arange(len(self.give_vec())):
#             args.append(self.give_vec()[k])
#         return args
#
#     def tracker_set_vals(self):
#         # use like "self.play(*spiky.tracker_set_vals())"
#         args = []
#         for i in np.arange(self.n):
#             temp_args = []
#             temp_args = self.tracker_set_val(i)
#             args.append(temp_args[0])
#             args.append(temp_args[1])
#             args.append(temp_args[2])
#         return args
#
#     def give_vec(self):
#         args = []
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 args.append(self.vec_draw[i][j])
#         return args
#
#     def animate_shift_mobjects(self, vector):
#         args = []
#         self.animate_shift_origins(vector)
#         vec_args = self.animate_shift_vec_draws(vector)
#         brack_args = self.animate_shift_brackets(vector)
#         ax_args = self.animate_shift_axes(vector)
#         for v in np.arange(len(vec_args)):
#             args.append(vec_args[v])
#         for b in np.arange(len(brack_args)):
#             args.append(brack_args[b])
#         for a in np.arange(len(ax_args)):
#             args.append(ax_args[a])
#         return args
#     # # Commented out because I don't want to finish the helper functions
#     # def shift_mobjects(self, vector):
#     #     self.shift_origins(vector)
#     #     self.shift_vec_draws(vector)
#     #     self.shift_brackets(vector)
#
#
# class SpikyVectorFromMethods(Scene):
#     cirhuh = False
#     n = 2
#     ax_range = 1
#     origins = [None] * n
#     axes = [None] * n
#     vec = np.empty((n,), dtype=complex)
#     vec_track = [[None]*3]*n
#     vec_draw = [[None]*3]*n
#     brackets = []
#     bracketL = Tex("\\Bigg[")
#     bracketR = Tex("\\Bigg]")
#     colorRe = BLUE
#     colorIm = RED
#     colorMod = WHITE
#
#     def __init__(self,cirhuh,n,ax_range,vec):
#         self.cirhuh = cirhuh
#         self.n = n
#         self.ax_range = ax_range
#         self.vec = vec
#         self.norm_vector()
#         self.origins = self.init_empty_list_of_lists(self.n,0)
#         self.axes = self.init_empty_list_of_lists(self.n,0)
#         self.vec_track = self.init_empty_list_of_lists(self.n,3)
#         self.vec_draw = self.init_empty_list_of_lists(self.n,3)
#
#         self.init_origins()
#         self.init_trackers()
#         self.set_trackers()
#         self.init_axes()
#         self.init_draw_vec()
#         self.init_draw_vec_updaters()
#         self.init_brackets()
#
#
#
#
#     ### INTERNAL METHODS
#     ## INIT PRIMARY METHODS
#     # (methods directly called in init function)
#     def norm_vector(self):
#         norms = np.linalg.norm(self.vec)
#         self.vec = self.vec / norms
#
#     def init_empty_list_of_lists(self,width,depth):
#         out = self.init_list_of_list(width)
#         for i in np.arange(width):
#             self.expand_empty_list(out[i],depth)
#         return out
#
#     def init_origins(self):
#         for i in np.arange(self.n):
#             self.origins[i] = (2*i - (self.n/2)) * UP * 1.5 * self.ax_range
#
#     def init_trackers(self):
#         for i in np.arange(self.n):
#             self.init_some_trackers(i)
#
#     def set_trackers(self):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.set_tracker(i,j)
#
#     def init_axes(self):
#         for i in np.arange(self.n):
#             self.axes[i] = ThreeDAxes(
#                 x_range=[-self.ax_range, self.ax_range, 1],
#                 y_range=[-self.ax_range, self.ax_range, 1],
#                 z_range=[0, self.ax_range, 1],
#                 x_length=self.ax_range,
#                 y_length=self.ax_range,
#                 z_length=self.ax_range,
#             ).move_to(self.origins[i]).shift(OUT * self.ax_range / 2)
#
#     def init_draw_vec(self):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.vec_draw[i][j] = self.make_draw_vec(i,j)
#
#     def init_draw_vec_updaters(self):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.give_updater(self.vec_draw[i][j],i,j)
#
#     def init_brackets(self):
#         self.brackets = []
#         self.bracketL = Tex("\\Bigg[")
#         self.bracketR = Tex("\\Bigg]")
#         self.bracketL.scale((3 * self.n * self.ax_range) / self.bracketL.get_height()).shift(LEFT * self.ax_range).shift(UP)
#         self.bracketR.scale((3 * self.n * self.ax_range) / self.bracketR.get_height()).shift(RIGHT * self.ax_range).shift(UP)
#         self.brackets.append(self.bracketL)
#         self.brackets.append(self.bracketR)
#
#
#     ## INIT SECONDARY METHODS
#     # (methods called in primary methods)
#     def init_list_of_list(self,width):
#         out = []
#         for i in np.arange(width):
#             out.append([])
#         return out
#     def expand_empty_list(self,list,depth):
#         for j in np.arange(depth):
#             list.append(None)
#
#     def init_some_trackers(self,i):
#         for j in np.arange(3):
#             self.vec_track[i][j] = self.make_tracker()
#     def make_tracker(self):
#         return ValueTracker()
#
#     def set_tracker(self,i,j):
#         if j == 0:
#             self.vec_track[i][j].set_value(np.real(self.vec[i]))
#         if j == 1:
#             self.vec_track[i][j].set_value(np.imag(self.vec[i]))
#         if j == 2:
#             self.vec_track[i][j].set_value(abs(self.vec[i]))
#
#     def make_draw_vec(self,i,j):
#         output_vec = None
#         vec_color, vec_dir = self.get_draw_vec_perams(j)
#
#         output_vec = Vector().set_color(vec_color)
#         output_vec.set_points_by_ends(self.origins[i],
#                                       self.origins[i] + self.vec_track[i][j].get_value() * vec_dir)
#         return output_vec
#     def get_draw_vec_perams(self,j):
#         vec_color = None
#         vec_dir = None
#         if j == 0:
#             vec_color = self.colorRe
#             vec_dir = RIGHT
#         if j == 1:
#             vec_color = self.colorIm
#             vec_dir = UP
#         if j == 2:
#             vec_color = self.colorMod
#             vec_dir = OUT
#         return vec_color, vec_dir
#
#     def give_updater(self,obj,i,j):
#         vec_dir = None
#         if j == 0:
#             vec_color = self.colorRe
#             vec_dir = RIGHT
#         if j == 1:
#             vec_color = self.colorIm
#             vec_dir = UP
#         if j == 2:
#             vec_color = self.colorMod
#             vec_dir = OUT
#         obj.add_updater(
#             lambda v: v.set_points_by_ends(self.origins[i],
#                                            self.origins[i] + self.vec_track[i][j].get_value() * vec_dir))
#
#     ## EXTERNAL SECONDARY METHODS
#     # (methods called for external methods)
#     def tracker_set_val(self,i):
#         args = []
#         args.append(self.vec_track[i][0].animate.set_value(np.real(self.vec[i])))
#         args.append(self.vec_track[i][1].animate.set_value(np.imag(self.vec[i])))
#         args.append(self.vec_track[i][2].animate.set_value(abs(self.vec[i])))
#         return args
#
#     def animate_shift_origins(self, vector):
#         for i in np.arange(self.n):
#             self.origins[i] = self.origins[i] + vector
#
#     def animate_shift_vec_draws(self, vector):
#         args = []
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 args.append(self.vec_draw[i][j].animate.shift(vector))
#         return args
#
#     def animate_shift_brackets(self, vector):
#         args = []
#         for i in np.arange(len(self.brackets)):
#             args.append(self.brackets[i].animate.shift(vector))
#         return args
#
#     def animate_shift_axes(self, vector):
#         args = []
#         for i in np.arange(len(self.axes)):
#             args.append(self.axes[i].animate.shift(vector))
#         return args
#
#     def shift_origins(self, vector):
#         for i in np.arange(self.n):
#             self.origins[i] = self.origins[i] + vector
#
#     def shift_vec_draws(self, vector):
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 self.vec_draw[i][j].shift(vector)
#
#     def shift_brackets(self, vector):
#         for i in np.arange(len(self.brackets)):
#             self.brackets[i].shift(vector)
#
#
#
#     ### EXTERNAL METHODS
#     # (methods that you should be using in your scene)
#     def add_all(self):
#         args = []
#         for i in np.arange(len(self.axes)):
#             args.append(self.axes[i])
#         for j in np.arange(len(self.brackets)):
#             args.append(self.brackets[j])
#         for k in np.arange(len(self.give_vec())):
#             args.append(self.give_vec()[k])
#         return args
#
#     def tracker_set_vals(self):
#         # use like "self.play(*spiky.tracker_set_vals())"
#         args = []
#         for i in np.arange(self.n):
#             temp_args = []
#             temp_args = self.tracker_set_val(i)
#             args.append(temp_args[0])
#             args.append(temp_args[1])
#             args.append(temp_args[2])
#         return args
#
#     def give_vec(self):
#         args = []
#         for i in np.arange(self.n):
#             for j in np.arange(3):
#                 args.append(self.vec_draw[i][j])
#         return args
#
#     def animate_shift_mobjects(self, vector):
#         args = []
#         self.animate_shift_origins(vector)
#         vec_args = self.animate_shift_vec_draws(vector)
#         brack_args = self.animate_shift_brackets(vector)
#         ax_args = self.animate_shift_axes(vector)
#         for v in np.arange(len(vec_args)):
#             args.append(vec_args[v])
#         for b in np.arange(len(brack_args)):
#             args.append(brack_args[b])
#         for a in np.arange(len(ax_args)):
#             args.append(ax_args[a])
#         return args
#     # # Commented out because I don't want to finish the helper functions
#     # def shift_mobjects(self, vector):
#     #     self.shift_origins(vector)
#     #     self.shift_vec_draws(vector)
#     #     self.shift_brackets(vector)
class SmoothieVector(Scene):
    n = 2
    ax_range = 1
    origins = [None] * n
    axes = [None] * n
    vec = np.empty((n,), dtype=complex)
    vec_track = [[None]*3]*n
    vec_draw = [[None]*3]*n
    brackets = []
    bracketL = Tex("\\Bigg[")
    bracketR = Tex("\\Bigg]")
    colorRe = BLUE
    colorIm = RED
    colorMod = WHITE

    def __init__(self,n,ax_range,vec):
        self.n = n
        self.ax_range = ax_range
        self.vec = vec
        self.norm_vector()
        self.origins = self.init_empty_list_of_lists(self.n,0)
        self.axes = self.init_empty_list_of_lists(self.n,0)
        self.vec_track = self.init_empty_list_of_lists(self.n,3)
        self.vec_draw = self.init_empty_list_of_lists(self.n,3)

        self.init_origins()
        self.init_trackers()
        self.set_trackers()
        self.init_axes()
        self.init_draw_vec()
        self.init_draw_vec_updaters()
        self.init_brackets()




    ### INTERNAL METHODS
    ## INIT PRIMARY METHODS
    # (methods directly called in init function)
    def norm_vector(self):
        norms = np.linalg.norm(self.vec)
        self.vec = self.vec / norms

    def init_empty_list_of_lists(self,width,depth):
        out = self.init_list_of_list(width)
        for i in np.arange(width):
            self.expand_empty_list(out[i],depth)
        return out

    def init_origins(self):
        for i in np.arange(self.n):
            self.origins[i] = (2*i - (self.n/2)) * UP * 1.5 * self.ax_range

    def init_trackers(self):
        for i in np.arange(self.n):
            self.init_some_trackers(i)

    def set_trackers(self):
        for i in np.arange(self.n):
            for j in np.arange(3):
                self.set_tracker(i,j)

    def init_axes(self):
        for i in np.arange(self.n):
            self.axes[i] = ThreeDAxes(
                x_range=[-self.ax_range, self.ax_range, 1],
                y_range=[-self.ax_range, self.ax_range, 1],
                z_range=[0, self.ax_range, 1],
                x_length=self.ax_range,
                y_length=self.ax_range,
                z_length=self.ax_range,
            ).move_to(self.origins[i]).shift(OUT * self.ax_range / 2)

    def init_draw_vec(self):
        for i in np.arange(self.n):
            for j in np.arange(3):
                self.vec_draw[i][j] = self.make_draw_vec(i,j)

    def init_draw_vec_updaters(self):
        for i in np.arange(self.n):
            for j in np.arange(2):
                self.give_updater(self.vec_draw[i][j],i,j)

    def init_brackets(self):
        self.brackets = []
        self.bracketL = Tex("\\Bigg[")
        self.bracketR = Tex("\\Bigg]")
        self.bracketL.scale((3 * self.n * self.ax_range) / self.bracketL.get_height()).shift(LEFT * self.ax_range)
        self.bracketR.scale((3 * self.n * self.ax_range) / self.bracketR.get_height()).shift(RIGHT * self.ax_range)
        self.brackets.append(self.bracketL)
        self.brackets.append(self.bracketR)


    ## INIT SECONDARY METHODS
    # (methods called in primary methods)
    def init_list_of_list(self,width):
        out = []
        for i in np.arange(width):
            out.append([])
        return out
    def expand_empty_list(self,list,depth):
        for j in np.arange(depth):
            list.append(None)

    def init_some_trackers(self,i):
        for j in np.arange(3):
            self.vec_track[i][j] = self.make_tracker()
    def make_tracker(self):
        return ValueTracker()

    def set_tracker(self,i,j):
        if j == 0:
            self.vec_track[i][j].set_value(np.real(self.vec[i]))
        if j == 1:
            self.vec_track[i][j].set_value(np.imag(self.vec[i]))
        if j == 2:
            self.vec_track[i][j].set_value(abs(self.vec[i]))

    def make_draw_vec(self,i,j):
        output_vec = None
        vec_color, vec_dir = self.get_draw_vec_perams(j)

        output_vec = Vector().set_color(vec_color)
        output_vec.set_points_by_ends(self.origins[i],
                                      self.origins[i] + self.vec_track[i][j].get_value() * vec_dir)
        return output_vec
    def get_draw_vec_perams(self,j):
        vec_color = None
        vec_dir = None
        if j == 0:
            vec_color = self.colorRe
            vec_dir = RIGHT
        if j == 1:
            vec_color = self.colorIm
            vec_dir = UP
        if j == 2:
            vec_color = self.colorMod
            vec_dir = OUT
        return vec_color, vec_dir

    def give_updater(self,obj,i,j):
        vec_dir = None
        if j == 0:
            obj.add_updater(
                lambda v: v.set_points_by_ends(self.origins[i],
                                               self.origins[i] +
                                               (self.vec_track[i][0].get_value() * RIGHT) +
                                               (self.vec_track[i][1].get_value() * UP)
                                               ))
        if j == 1:
            obj.add_updater(
                lambda v: v.set_points_by_ends(self.origins[i],
                                               self.origins[i] +
                                               (self.vec_track[i][2].get_value() * OUT)
                                               ))


    ## EXTERNAL SECONDARY METHODS
    # (methods called for external methods)
    def tracker_set_val(self,i):
        args = []
        args.append(self.vec_track[i][0].animate.set_value(np.real(self.vec[i])))
        args.append(self.vec_track[i][1].animate.set_value(np.imag(self.vec[i])))
        args.append(self.vec_track[i][2].animate.set_value(abs(self.vec[i])))
        return args

    def animate_shift_origins(self, vector):
        for i in np.arange(self.n):
            self.origins[i] = self.origins[i] + vector

    def animate_shift_vec_draws(self, vector):
        args = []
        for i in np.arange(self.n):
            for j in np.arange(3):
                args.append(self.vec_draw[i][j].animate.shift(vector))
        return args

    def animate_shift_brackets(self, vector):
        args = []
        for i in np.arange(len(self.brackets)):
            args.append(self.brackets[i].animate.shift(vector))
        return args

    def animate_shift_axes(self, vector):
        args = []
        for i in np.arange(len(self.axes)):
            args.append(self.axes[i].animate.shift(vector))
        return args

    def shift_origins(self, vector):
        for i in np.arange(self.n):
            self.origins[i] = self.origins[i] + vector

    def shift_vec_draws(self, vector):
        for i in np.arange(self.n):
            for j in np.arange(3):
                self.vec_draw[i][j].shift(vector)

    def shift_brackets(self, vector):
        for i in np.arange(len(self.brackets)):
            self.brackets[i].shift(vector)



    ### EXTERNAL METHODS
    # (methods that you should be using in your scene)
    def add_all(self):
        args = []
        for i in np.arange(len(self.axes)):
            args.append(self.axes[i])
        for j in np.arange(len(self.brackets)):
            args.append(self.brackets[j])
        for k in np.arange(len(self.give_vec())):
            args.append(self.give_vec()[k])
        return args

    def tracker_set_vals(self):
        # use like "self.play(*spiky.tracker_set_vals())"
        args = []
        for i in np.arange(self.n):
            temp_args = []
            temp_args = self.tracker_set_val(i)
            args.append(temp_args[0])
            args.append(temp_args[1])
            args.append(temp_args[2])
        return args

    def give_vec(self):
        args = []
        for i in np.arange(self.n):
            for j in np.arange(3):
                args.append(self.vec_draw[i][j])
        return args

    def animate_shift_mobjects(self, vector):
        args = []
        self.animate_shift_origins(vector)
        vec_args = self.animate_shift_vec_draws(vector)
        brack_args = self.animate_shift_brackets(vector)
        ax_args = self.animate_shift_axes(vector)
        for v in np.arange(len(vec_args)):
            args.append(vec_args[v])
        for b in np.arange(len(brack_args)):
            args.append(brack_args[b])
        for a in np.arange(len(ax_args)):
            args.append(ax_args[a])
        return args
    # # Commented out because I don't want to finish the helper functions
    # def shift_mobjects(self, vector):
    #     self.shift_origins(vector)
    #     self.shift_vec_draws(vector)
    #     self.shift_brackets(vector)


class SpikyVector(Scene):
    cirhuh = False
    n = 2
    ax_range = 1
    origins = [None] * n
    axes = [None] * n
    vec = np.empty((n,), dtype=complex)
    vec_track = [[None]*3]*n
    vec_draw = [[None]*3]*n
    brackets = []
    bracketL = Tex("\\Bigg[")
    bracketR = Tex("\\Bigg]")
    colorRe = BLUE
    colorIm = RED
    colorMod = WHITE

    def __init__(self,cirhuh,n,ax_range,vec):
        self.cirhuh = cirhuh
        self.n = n
        self.ax_range = ax_range
        self.vec = vec
        self.norm_vector()
        self.origins = self.init_empty_list_of_lists(self.n,0)
        self.axes = self.init_empty_list_of_lists(self.n,0)
        self.vec_track = self.init_empty_list_of_lists(self.n,3)
        self.vec_draw = self.init_empty_list_of_lists(self.n,3)

        self.init_origins()
        self.init_trackers()
        self.set_trackers()
        self.init_axes()
        self.init_draw_vec()
        self.init_draw_vec_updaters()
        self.init_brackets()




    ### INTERNAL METHODS
    ## INIT PRIMARY METHODS
    # (methods directly called in init function)
    def norm_vector(self):
        norms = np.linalg.norm(self.vec)
        self.vec = self.vec / norms

    def init_empty_list_of_lists(self,width,depth):
        out = self.init_list_of_list(width)
        for i in np.arange(width):
            self.expand_empty_list(out[i],depth)
        return out

    def init_origins(self):
        for i in np.arange(self.n):
            self.origins[i] = (2*i - (self.n/2)) * UP * 1.5 * self.ax_range

    def init_trackers(self):
        for i in np.arange(self.n):
            self.init_some_trackers(i)

    def set_trackers(self):
        for i in np.arange(self.n):
            for j in np.arange(3):
                self.set_tracker(i,j)

    def init_axes(self):
        for i in np.arange(self.n):
            self.axes[i] = ThreeDAxes(
                x_range=[-self.ax_range, self.ax_range, 1],
                y_range=[-self.ax_range, self.ax_range, 1],
                z_range=[0, self.ax_range, 1],
                x_length=self.ax_range,
                y_length=self.ax_range,
                z_length=self.ax_range,
            ).move_to(self.origins[i]).shift(OUT * self.ax_range / 2)

    def init_draw_vec(self):
        for i in np.arange(self.n):
            for j in np.arange(3):
                self.vec_draw[i][j] = self.make_draw_vec(i,j)

    def init_draw_vec_updaters(self):
        for i in np.arange(self.n):
            for j in np.arange(3):
                self.give_updater(self.vec_draw[i][j],i,j)

    def init_brackets(self):
        self.brackets = []
        self.bracketL = Tex("\\Bigg[")
        self.bracketR = Tex("\\Bigg]")
        self.bracketL.scale((3 * self.n * self.ax_range) / self.bracketL.get_height()).shift(LEFT * self.ax_range).shift(UP)
        self.bracketR.scale((3 * self.n * self.ax_range) / self.bracketR.get_height()).shift(RIGHT * self.ax_range).shift(UP)
        self.brackets.append(self.bracketL)
        self.brackets.append(self.bracketR)


    ## INIT SECONDARY METHODS
    # (methods called in primary methods)
    def init_list_of_list(self,width):
        out = []
        for i in np.arange(width):
            out.append([])
        return out
    def expand_empty_list(self,list,depth):
        for j in np.arange(depth):
            list.append(None)

    def init_some_trackers(self,i):
        for j in np.arange(3):
            self.vec_track[i][j] = self.make_tracker()
    def make_tracker(self):
        return ValueTracker()

    def set_tracker(self,i,j):
        if j == 0:
            self.vec_track[i][j].set_value(np.real(self.vec[i]))
        if j == 1:
            self.vec_track[i][j].set_value(np.imag(self.vec[i]))
        if j == 2:
            self.vec_track[i][j].set_value(abs(self.vec[i]))

    def make_draw_vec(self,i,j):
        output_vec = None
        vec_color, vec_dir = self.get_draw_vec_perams(j)

        output_vec = Vector().set_color(vec_color)
        output_vec.set_points_by_ends(self.origins[i],
                                      self.origins[i] + self.vec_track[i][j].get_value() * vec_dir)
        return output_vec
    def get_draw_vec_perams(self,j):
        vec_color = None
        vec_dir = None
        if j == 0:
            vec_color = self.colorRe
            vec_dir = RIGHT
        if j == 1:
            vec_color = self.colorIm
            vec_dir = UP
        if j == 2:
            vec_color = self.colorMod
            vec_dir = OUT
        return vec_color, vec_dir

    def give_updater(self,obj,i,j):
        vec_dir = None
        if j == 0:
            vec_color = self.colorRe
            vec_dir = RIGHT
        if j == 1:
            vec_color = self.colorIm
            vec_dir = UP
        if j == 2:
            vec_color = self.colorMod
            vec_dir = OUT
        obj.add_updater(
            lambda v: v.set_points_by_ends(self.origins[i],
                                           self.origins[i] + self.vec_track[i][j].get_value() * vec_dir))

    ## EXTERNAL SECONDARY METHODS
    # (methods called for external methods)
    def tracker_set_val(self,i):
        args = []
        args.append(self.vec_track[i][0].animate.set_value(np.real(self.vec[i])))
        args.append(self.vec_track[i][1].animate.set_value(np.imag(self.vec[i])))
        args.append(self.vec_track[i][2].animate.set_value(abs(self.vec[i])))
        return args

    def animate_shift_origins(self, vector):
        for i in np.arange(self.n):
            self.origins[i] = self.origins[i] + vector

    def animate_shift_vec_draws(self, vector):
        args = []
        for i in np.arange(self.n):
            for j in np.arange(3):
                args.append(self.vec_draw[i][j].animate.shift(vector))
        return args

    def animate_shift_brackets(self, vector):
        args = []
        for i in np.arange(len(self.brackets)):
            args.append(self.brackets[i].animate.shift(vector))
        return args

    def animate_shift_axes(self, vector):
        args = []
        for i in np.arange(len(self.axes)):
            args.append(self.axes[i].animate.shift(vector))
        return args

    def shift_origins(self, vector):
        for i in np.arange(self.n):
            self.origins[i] = self.origins[i] + vector

    def shift_vec_draws(self, vector):
        for i in np.arange(self.n):
            for j in np.arange(3):
                self.vec_draw[i][j].shift(vector)

    def shift_brackets(self, vector):
        for i in np.arange(len(self.brackets)):
            self.brackets[i].shift(vector)



    ### EXTERNAL METHODS
    # (methods that you should be using in your scene)
    def add_all(self):
        args = []
        for i in np.arange(len(self.axes)):
            args.append(self.axes[i])
        for j in np.arange(len(self.brackets)):
            args.append(self.brackets[j])
        for k in np.arange(len(self.give_vec())):
            args.append(self.give_vec()[k])
        return args

    def tracker_set_vals(self):
        # use like "self.play(*spiky.tracker_set_vals())"
        args = []
        for i in np.arange(self.n):
            temp_args = []
            temp_args = self.tracker_set_val(i)
            args.append(temp_args[0])
            args.append(temp_args[1])
            args.append(temp_args[2])
        return args

    def give_vec(self):
        args = []
        for i in np.arange(self.n):
            for j in np.arange(3):
                args.append(self.vec_draw[i][j])
        return args

    def animate_shift_mobjects(self, vector):
        args = []
        self.animate_shift_origins(vector)
        vec_args = self.animate_shift_vec_draws(vector)
        brack_args = self.animate_shift_brackets(vector)
        ax_args = self.animate_shift_axes(vector)
        for v in np.arange(len(vec_args)):
            args.append(vec_args[v])
        for b in np.arange(len(brack_args)):
            args.append(brack_args[b])
        for a in np.arange(len(ax_args)):
            args.append(ax_args[a])
        return args
    # # Commented out because I don't want to finish the helper functions
    # def shift_mobjects(self, vector):
    #     self.shift_origins(vector)
    #     self.shift_vec_draws(vector)
    #     self.shift_brackets(vector)
