import wpf
import math

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'CEPH_pg_calc.xaml')
        
    def Button_Click(self, sender, e):
        a = float(self.textBoxOSD.Text)
        b = float(self.textBoxSize.Text)
        n = a * 100 / b
        def power_two(n):
            return int(math.log(n, 2))
        p = 2**power_two(n)


        self.labelResult.Content = str(p)

if __name__ == '__main__':
    Application().Run(MyWindow())
