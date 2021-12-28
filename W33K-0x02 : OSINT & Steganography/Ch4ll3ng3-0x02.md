# Ch4ll3ng3-0x02.md

This challenge is taken from a TryHackMe room called OhSINT useful to train your OSINT skills

The image seems to be a Windows XP typical background. You can get it from here:
https://drive.google.com/file/d/1VpqpwTnBOlzsAWhsWRUm_DZGDWVmtm6R/view

![WindowsXP](https://user-images.githubusercontent.com/79013612/147607224-d6c3b7b9-6ee7-4738-9795-b7523c52ed10.jpg)

## Q1: What is this user's avatar? 

We will start by executing exiftool on the image to see if something will lead us to the user

![2021-12-28 21_51_41-Kali-Linux-2021 3-vbox-amd64  En fonction  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/79013612/147606188-02ed9e97-1a3c-41f3-a9e3-a19ca0a107f5.png)

![2021-12-28 21_52_00-Kali-Linux-2021 3-vbox-amd64  En fonction  - Oracle VM VirtualBox](https://user-images.githubusercontent.com/79013612/147606194-90e9bdb9-adc4-489a-a54a-0925b98732ac.png)

We gol the name **OWoodFlint**

If Google the name we will get lot of results

![2021-12-28 21_54_24-OWoodflint - Google Search and 7 more pages - Personal - Microsoft​ Edge](https://user-images.githubusercontent.com/79013612/147606323-ae3d4ddf-17f6-43b6-9f17-8aa3169be365.png)

In the twitter account we can see that the answer is a **cat**

## Q2: What city is this person in?

By visiting OWoodFlint repository in github we will find

![2021-12-28 21_57_19-OWoodfl1nt_people_finder_ A new social network for taking photos in your home to](https://user-images.githubusercontent.com/79013612/147606527-40413519-abf6-45bb-a732-343bf8f52291.png)

The answer is **London**

## Q3: What is his personal email address? 

The answer is **OWoodflint@gmail.com**

## Q4: What site did you find his email address on? 

The answer is **GitHub**

## Q5: Where has he gone on holiday? 

By visiting his WordPress Blog we find  

![2021-12-28 21_59_08-owoodflint – Oliver Woodflint Blog and 7 more pages - Personal - Microsoft​ Edge](https://user-images.githubusercontent.com/79013612/147606605-e19b2614-1870-403a-b76a-1aa5441dc89c.png)

The answer is **New York**

## Q6: What is this person's password?

In this question, the answer is in the WordPress website but it is a clear text with a white font color so it can't be seen with the eye. Using CTRL+A we select all the text in the page and we find the answer

![2021-12-28 22_04_42-owoodflint – Oliver Woodflint Blog and 7 more pages - Personal - Microsoft​ Edge](https://user-images.githubusercontent.com/79013612/147606997-039c6d14-6b2b-4027-9bf7-9fc44db9b916.png)


The answer is **pennYDr0pper.!**
