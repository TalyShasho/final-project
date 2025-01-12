README



      “Data descripción”
The dataset includes fMRI and heart rate data from 52 participants, who underwent structured experiments with various music stimuli. 
This dataset is particularly suitable for this research because it provides detailed measurements of insula activity, heart rate, 
and interoceptive sensitivity in a controlled environment, enabling the analysis of time-dependent neural and physiological changes.

     “Project goals”
This project investigates how pysiological activity, like heart rate change depending on the type of music and the time spent listening and what role  
plays interoceptive sensitivity in it.

       “Process”
1. We manage a large amount of data for each subject. The specific data we need is stored in a single file within multiple nested folders.
To address this challenge, we developed a script that navigates through each subject's folder, extracts the relevant files,
and compiles their information into a single Excel file.
The data was spred throgh 6 files for each subject some divided by just by subject and some divided also by session.
To adress this we created 3 files of our own so the code and data wolud be cleares and then merge them to have everything in just one file.

2.We wanted to see if there is a correlation between type of music and Emocional response. For this we used Pearson coeficient.

3.We did an histogram to see how the emotional response change depending on the type of music.

4.
