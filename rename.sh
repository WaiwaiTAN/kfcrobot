sed -i "s/基座装配图.png/Assembly_drawing.png/g" `grep 基座装配图.png -rl ./`
sed -i "s/机械手装配图.png/Robot_assembly_drawing.png/g" `grep 机械手装配图.png -rl ./`
sed -i "s/机械臂装配图.png/Robot_arm_assembly_drawing.png/g" `grep 机械臂装配图.png -rl ./`
sed -i "s/expenditure_statistics.tex/expenditure_statistics.tex/g" `grep expenditure_statistics.tex -rl ./`
