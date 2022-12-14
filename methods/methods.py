from ref.hold_constants import *

class lilGuy(Scene):
    text = Tex("\\ket{\\psi}")
    text_color = GREY_B
    scale = .7
    pup_radius = scale / 2
    eye_width = scale * 2
    eye_height = scale * 4
    char_scale = scale * 5
    look = "right"
    eye_white_left = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
    eye_white_right = Ellipse(width=eye_width, height=eye_height, color=WHITE, fill_opacity=1)
    pupil_left = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
        eye_white_left.get_right() + pup_radius * LEFT)
    pupil_right = Circle(radius=pup_radius, color=BLACK, fill_opacity=1).move_to(
        eye_white_right.get_right() + pup_radius * LEFT)
    eye_left = VGroup(eye_white_left, pupil_left).shift(LEFT * eye_width)
    eye_right = VGroup(eye_white_right, pupil_right).shift(RIGHT * eye_width)
    eyes = VGroup(eye_left, eye_right).scale(1 / 5).shift(RIGHT * .1)
    char = text.set_color(text_color).scale(char_scale)
    lilguy = VGroup(char, eyes)

    def __init__(self,text=Tex("\\ket{\\psi}"),text_color = GREY_B, scale = .7, look = "right"
                 ):
        self.text = text
        self.text_color = text_color
        self.scale = scale
        self.look = look
        self.pup_radius = self.scale / 2
        self.eye_width = self.scale * 2
        self.eye_height = self.scale * 4
        self.char_scale = self.scale * 5
        self.eye_white_left = Ellipse(width=self.eye_width, height=self.eye_height, color=WHITE, fill_opacity=1)
        self.eye_white_right = Ellipse(width=self.eye_width, height=self.eye_height, color=WHITE, fill_opacity=1)
        if self.look == "right":
            self.pupil_left = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_left.get_right() + self.pup_radius * LEFT)
            self.pupil_right = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_right.get_right() + self.pup_radius * LEFT)
        if self.look == "left":
            self.pupil_left = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_left.get_left() + self.pup_radius * RIGHT)
            self.pupil_right = Circle(radius=self.pup_radius, color=BLACK, fill_opacity=1).move_to(
                self.eye_white_right.get_left() + self.pup_radius * RIGHT)

        self.eye_left = VGroup(self.eye_white_left, self.pupil_left).shift(LEFT * self.eye_width)
        self.eye_right = VGroup(self.eye_white_right, self.pupil_right).shift(RIGHT * self.eye_width)
        self.eyes = VGroup(self.eye_left, self.eye_right).scale(1 / 5).shift(RIGHT * .1)
        if self.look == "right":
            self.eyes.shift(RIGHT * .1)
        if self.look == "left":
            self.eyes.shift(LEFT * .1)
        self.text.set_color(self.text_color).scale(self.char_scale)
        self.lilguy = VGroup(self.text, self.eyes)

    def shift(self,vector):
        self.lilguy.shift(vector)

    def eyes_follow(self,Point):
        for i in np.arange(2):
            self.eye_follow(Point, i)

    def eye_follow(self,Point,i):
        dir = self.get_eye_follow_dir()
        self.eyes[i][1].add_updater(
            lambda p: p.move_to()
        )

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

def prop_sig_x(dt):
    prop_diag = np.diag(np.exp(-1j * dt * x_vals))
    return np.dot(x_U, np.dot(prop_diag, x_U_dag))

def prop_sig_y(dt):
    prop_diag = np.diag(np.exp(-1j * dt * y_vals))
    return np.dot(y_U, np.dot(prop_diag, y_U_dag))

def prop_sig_z(dt):
    prop_diag = np.diag(np.exp(-1j * dt * z_vals))
    return np.dot(z_U, np.dot(prop_diag, z_U_dag))

def prop_gen(dt, basis):
    # Make our propogator
    if basis == "x":
        propogator = prop_sig_x(dt)
    elif basis == "y":
        propogator = prop_sig_y(dt)
    elif basis == "z":
        propogator = prop_sig_z(dt)
    return propogator

def prop_sig_z_pert(dt):
    prop_diag = np.diag(np.exp(-1j * dt * z_pert_vals))
    return np.dot(z_pert_U, np.dot(prop_diag, z_pert_U_dag))

def create_evolver(matrix,dt):
    norms = np.linalg.norm(matrix, axis=1)
    normed = matrix/norms
    eigenvalues, m_U = np.linalg.eig(normed)
    m_U_dag = np.linalg.inv(m_U)
    diag = np.diag(np.exp(-1j * dt * eigenvalues))
    return np.dot(m_U, np.dot(diag, m_U_dag))

def improper_evolver(matrix,dt):
    # Evolves without returning to the regular basis
    norms = np.linalg.norm(matrix, axis=1)
    normed = matrix/norms
    eigenvalues, m_U = np.linalg.eig(normed)
    m_U_dag = np.linalg.inv(m_U)
    diag = np.diag(np.exp(-1j * dt * eigenvalues))
    return diag


def fade_out_all(list):
    args = []
    for i in np.arange(len(list)):
        args.append(FadeOut(list[i]))
    return args


def fade_in_all(list):
    args = []
    for i in np.arange(len(list)):
        args.append(FadeIn(list[i]))
    return args
