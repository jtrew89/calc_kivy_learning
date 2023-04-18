##if the design aspect of the app is in a design kivy file, you do not need to import design modules

import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#set the app window size
Window.size = (400,600)

#builder allows you to use specific design files for specic portions of the app, so that you can use more than 1
Builder.load_file('calc.kv')

##make grid for app
class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = '0'
	#Button pressing function
	def button_press(self, button):
		#variable that contains whatever was in the text box already
		prior = self.ids.calc_input.text

		#test for error first
		if prior == 'Error':
			prior = ''
		#determine if 0 i in place
		if prior == '0':
			self.ids.calc_input.text = ''
			self.ids.calc_input.text = f'{button}'
		elif prior == '-0':
			pass

		else:
			self.ids.calc_input.text = f'{prior}{button}'

	#create addition function
	def math_operator(self, sign):
		
		#variable of value already in unput text box
		prior = self.ids.calc_input.text
		
		#include + sign to text box
		self.ids.calc_input.text = f'{prior}{sign}'

	#create equals function
	def equals(self):
		prior = self.ids.calc_input.text
		#error handling
		try:
			#evaluate the math from the input box
			answer = eval(prior)
			#output answer
			self.ids.calc_input.text = str(answer)
		except:
			self.ids.calc_input.text = 'Error'

		'''
		#Addition
		if '+' in prior:
			num_list = prior.split('+')
			answer = 0.0

			#loop through list
			for num in num_list:
				answer = answer + float(num)

			#print answer in the text box
			self.ids.calc_input.text = str(answer)
			'''

	#create function to remove last character on input screen
	def remove(self):
		prior = self.ids.calc_input.text
		#remove last character in input box and reassign
		prior = prior[:-1]
		#output back to input box
		self.ids.calc_input.text = prior

	#Create function to make input box positive or negative
	def pos_neg(self):
		prior = self.ids.calc_input.text

		#check to see if there is already a subtraction sign
		if '-' in prior:
			self.ids.calc_input.text = f"{prior.replace('-', '')}"
		else:
			self.ids.calc_input.text = f'-{prior}'

	#create decimal function
	def dot(self):
		prior = self.ids.calc_input.text

		#split input into separate input numbers
		num_list = prior.split('+')

		if '+' in prior and '.' not in num_list[-1]:
			prior = f'{prior}.'

			#output back to text box
			self.ids.calc_input.text = prior
		elif '.' in prior:
			pass
		else:
			prior = f'{prior}.'

			#output back to text box
			self.ids.calc_input.text = prior
class CalculatorApp(App): #whatever the build class is called, the supporting kivy design file must be named similarly (without capital letters), e.g. my.kv. This file has to be in the same directory, that is why there is no reference to it
    
    def build(self):
        return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()