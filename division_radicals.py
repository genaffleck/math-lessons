from manim import *

from manim._config.utils import ManimConfig

ManimConfig.background_color = "#ece6e2"

class Intro(Scene):
  def construct(self):
    code = """Division of Radicals
    """

    codes = Code(
      code =code,
      tab_width=12,
      background_stroke_width=5,
      background_stroke_color=DARK_GREY,
      insert_line_no=False,
      style=Code.styles_list[14],
      background="window",
      language="latex"
    ).scale(2).shift(UP)

    self.wait()
    self.play(Write(codes))
    self.wait()

class division_rule(Scene):
  def construct(self):
    div_rule = MathTex(r"\sqrt[n]{\frac{a}{b}}=\frac{\sqrt[n]{a}}{\sqrt[n]{b}}", font_size = 120).set_color(BLACK)
    
    code = """Rule for Division"""

    codes = Code(
      code =code,
      tab_width=12,
      background_stroke_width=5,
      background_stroke_color=DARK_GREY,
      insert_line_no=False,
      style=Code.styles_list[20],
      background="window",
      language="python"
    ).scale(0.5).shift(UP*3.1+LEFT*5)

    self.wait()
    self.play(Write(codes))
    self.play(Write(div_rule), run_time = 3)
    self.wait()
    
class division_example1(Scene):
  def construct(self):
    eqn = MathTex(r"\textrm{Simplify}\ \frac{2}{\sqrt{3}}", font_size=70).shift(UP*3+LEFT*1.25).set_color(BLACK)
    step1 = MathTex(
      r"& = \frac{2}{\sqrt{3}}\cdot\frac{\sqrt{3}}{\sqrt{3}}\\",
      r"& = \frac{2\sqrt{3}}{3}",
      font_size = 70
    ).next_to(eqn, DOWN*3).set_color(DARK_GRAY)
    
    implies = MathTex(r"\rightarrow", font_size = 50).next_to(step1[0], RIGHT, buff=0.5).set_color(PURE_RED)
    step1_text = MathTex(r"\boldmath{rationalize\ the}\\",
      r"denominator",
      font_size = 50
    ).next_to(implies, RIGHT*1.2, buff=0.5).set_color(PURE_RED)
    
    code = """
    Example 1 
      """

    codes = Code(
      code =code,
      tab_width=6,
      background_stroke_width=1,
      background_stroke_color=DARK_GREY,
      insert_line_no=False,
      style=Code.styles_list[11],
      background="window",
      language="latex"
    ).scale(0.5).shift(UP*3.1+LEFT*5)
    # animations
    
    self.wait()
    self.play(Write(codes), run_time=2)
    self.wait()
    self.play(Write(eqn), run_time=3)
    self.wait(4)
    self.play(Write(step1[0]), run_time=3)
    self.wait()
    self.play(Write(implies))
    self.play(Write(step1_text))
    self.wait(2)
    self.play(Write(step1[1]), run_time=3)
    self.wait(2)

class division_example2(Scene):
  def construct(self):
    eqn1 = MathTex(
      r"& \textrm{Simplify}\ \sqrt{\frac{5}{6}}",
      font_size=70).shift(UP*3+LEFT*1.25).set_color(BLACK)
    step_1 = MathTex(
      r"\sqrt{\frac{5}{6}} & = \frac{\sqrt{5}}{\sqrt{6}}\cdot\frac{\sqrt{6}}{\sqrt{6}}\\",
      r"& = \frac{\sqrt{30}}{6}",
      font_size = 70
    ).next_to(eqn1, DOWN*3).set_color(DARK_GRAY)
    
    implies2 = MathTex(r"\rightarrow", font_size = 50).next_to(step_1[0], RIGHT, buff=0.5).set_color(PURE_RED)
    step1_txt = MathTex(r"& rationalize\ the\\",
      r"& denominator",
      font_size = 50
    ).next_to(implies2, RIGHT*1.2, buff=0.5).set_color(PURE_RED)
    
    code = """
    Example 2 
      """

    codes = Code(
      code =code,
      tab_width=6,
      background_stroke_width=1,
      background_stroke_color=DARK_GREY,
      insert_line_no=False,
      style=Code.styles_list[11],
      background="window",
      language="latex"
    ).scale(0.5).shift(UP*3+LEFT*4.75)
    # animations
    
    self.wait()
    self.play(Write(codes), run_time=2)
    self.wait()
    self.play(Write(eqn1), run_time=3)
    self.wait(4)
    self.play(Write(step_1[0]), run_time=3)
    self.wait(2)
    self.play(Write(implies2))
    self.play(Write(step1_txt))
    self.wait(2)
    self.play(Write(step_1[1]), run_time=3)
    self.wait(2)

class division_example3(Scene):
  def construct(self):
    eqn3 = MathTex(
      r"& \textrm{Rationalize the denominator of}\ \frac{3}{5\sqrt{2}}",
      font_size=60).shift(UP*3).set_color(BLACK)
    eqn3_step_1 = MathTex(
      r"& =\frac{3}{5\sqrt{2}}\cdot\frac{\sqrt{2}}{\sqrt{2}}\\",
      r"& = \frac{3\sqrt{2}}{5\cdot 2}\\",
      r"& = \frac{3\sqrt{2}}{10}",
      font_size = 70
    ).set_color(DARK_GRAY).shift(LEFT+DOWN*0.75)
        
    code = """
    Example 3 
      """

    codes = Code(
      code =code,
      tab_width=6,
      background_stroke_width=1,
      background_stroke_color=DARK_GREY,
      insert_line_no=False,
      style=Code.styles_list[11],
      background="window",
      language="latex"
    ).scale(0.5).shift(UP*3.1+LEFT*6)
    # animations
    
    self.wait()
    self.play(Write(codes), run_time=2)
    self.wait()
    self.play(Write(eqn3), run_time=3)
    self.wait(4)
    self.play(Write(eqn3_step_1[0]), run_time=3)
    self.wait(2)
    self.play(Write(eqn3_step_1[1]), run_time=3)
    self.wait(2)
    self.play(Write(eqn3_step_1[2]), run_time=3)
    self.wait(2)