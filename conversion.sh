#!/bin/bash
#DSL

echo "Please enter your first and last name."
read fname lname
echo "Please enter your weight in lbs."
read weight_lb
echo "Please enter height in in."
read height_in

weight_kg=`echo "scale = 1; $weight_lb * 0.453592" | bc -l`
height_cm=`echo "scale = 2; $height_in * 2.54" | bc -l`
height_m=`echo $height_cm/100 | bc -l`
BMI=`echo "scale = 2; $weight_kg / $height_m^2" | bc -l`

echo "Name: $fname $lname"
echo "Weight in kg: $weight_kg"
echo "Height in cm: $height_cm"
echo "BMI: $BMI"
