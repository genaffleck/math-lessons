from manim import *

class radicalDivision_1(Scene):
  def construct(self):
    self.camera.background_color = "#ece6e2"
   
    question = MathTex(
      r"\textrm{Divide and simplify:}",
      r"\ \dfrac{3}{\sqrt{2}}",
      font_size=80
    ).set_color(BLACK).shift(UP*2.75)
   
    code = """
      Example 1
    """
    codes = Code(
      code=code,
      tab_width=3,
      background_stroke_width=3,
      background_stroke_color=WHITE,
      insert_line_no=False,
      style=Code.styles_list[14],
      background="window",
      language="python"
    ).scale(0.5).next_to(question, LEFT, buff=0.5).shift(UP*0.1)

     
    fraction = MathTex(
      r"3",
      r"\over",
      r"\sqrt{2}",
      font_size=80
    ).set_color(BLACK).shift(LEFT*1.5+UP*0.5)
    
    cdot = MathTex(
      r"\cdot",
      font_size=80
    ).next_to(fraction).shift(UP*0.05).set_color(BLACK)
    
    rationalize = MathTex(
      r"\sqrt{2}",
      r"\over",
      r"\sqrt{2}",
      font_size=80
    ).set_color(BLACK).next_to(cdot).shift(UP*0.05)
      
    line2 = MathTex(
      r"3\sqrt{2}", r"\over", r"2",
      font_size = 80
    ).set_color(BLACK).next_to(fraction,DOWN)
    
    equal = MathTex(r"=", font_size=80).set_color(BLACK).next_to(line2, LEFT).shift(DOWN*0.15)
    
    # animations

    self.play(Write(codes))
    self.wait()
    self.play(Write(question))
    self.wait(2)
    self.play(Write(fraction))
    self.wait()
    self.play(Write(cdot))
    self.play(Write(rationalize[1]))
    self.wait(2)
    self.play(fraction[2].animate.set_color(PURE_RED))
    self.wait(2)
    self.play(AnimationGroup(
      TransformFromCopy(fraction[2], rationalize[0]),
      TransformFromCopy(fraction[2], rationalize[2]),
      fraction[2].animate.set_color(BLACK)
      ),
      run_time=2
    )
    self.wait(2)
    self.play(Write(equal))
    self.play(Write(line2[1]))
    self.play(AnimationGroup(
        fraction[0].animate.set_color(PURE_RED),
        rationalize[0].animate.set_color(PURE_RED),
        rationalize[2].animate.set_color(BLACK)
      )
    )
    self.wait(2)
    self.play(Write(line2[0]))
    self.wait(2)
    self.play(AnimationGroup(
        fraction[0].animate.set_color(BLACK),
        rationalize[0].animate.set_color(BLACK),
        fraction[2].animate.set_color(PURE_RED),
        rationalize[2].animate.set_color(PURE_RED)
      )
    )
    self.play(AnimationGroup(
        Write(line2[2], run_time=3),
        fraction[2].animate.set_color(BLACK),
        rationalize[2].animate.set_color(BLACK)
      ), run_time=2
    )
    self.wait(5)