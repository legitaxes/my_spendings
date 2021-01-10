# 💸 My Spendings shows you how much money you have wasted on ```microtransaction``` on Google Play
This simple program makes you regret your many life decisions made on stupid mobages or your other spendings on Google Play.

Some code and instructions has to be tweaked before if you want to customize this to get transaction for example `Steam` _or i could just make it work with steam as well_ 

It requires you to login to your gmail account through this application I have made

> This project is still a WIP and the future plan is to export the results (Date, What shit you spent on, price(check for usd)) 
> into an excel sheet so you can see an overview of your stupid life decisions

_This is project is meant for myself so that I do not have to manually keep track of my spendings by entering in the details manually_

## NOTE 📝
**This program does not work properly if you have 2FA turned on for your gmail account**
Instead, follow the instructions [here](https://support.google.com/accounts/answer/185833) to find out how to login with 2FA enabled

I have also realized I could have done this the easy way by doing this on [UIPath](https://www.uipath.com/)...

But I guess this is some good practice for python

---

## How it works 🛠
The program retrieves your emails from the ```Starred``` folder with the title ```Your Google Play Order Receipt```

After it retrieves, it should export out the results into an excel sheet to see an overview of the expenditure


## Instructions/Set-Up 🔨
1. Search your email using the search bar with this title ```Your Google Play Order Receipt``` and press ```enter```
![Search](https://media.discordapp.net/attachments/314385034461315072/795655362761719838/unknown.png) 

2. Move ALL of the found results into the ```Starred``` folder (using click and drag to the folder)
![Move](https://media.discordapp.net/attachments/314385034461315072/795656071079395349/unknown.png)

Next we will create a filter that filters all incoming message with the Subject Title ```Your Google Play Order Receipt```


1. Click on **Settings** > **See All Settings** > **Filters and Blocked Addresses**

![Click](https://media.discordapp.net/attachments/314385034461315072/795656374938763284/unknown.png)

2. Click on **Create a new filter** and under the Subject, enter ```Your Google Play Order Receipt```
![Click](https://media.discordapp.net/attachments/314385034461315072/795656607266373664/unknown.png)

3. Then click on **Create filter** which will bring you to the _action_ part of the filter
![Click](https://media.discordapp.net/attachments/314385034461315072/795656748941180968/unknown.png)

4. **Check** the checkbox ```Star it``` and click ```Create filter```
![Check](https://media.discordapp.net/attachments/314385034461315072/795656898988605470/unknown.png)

5. Profit: ∞?

_Doing this will **star** all your future incoming messages with the title ```Your Google Play Order Receipt``` which then you can run the program again to get the updated results_

---

## Question 🟣
Q: Is this safe to have app password created and enabled?

  A: I cannot guarantee your safety of your Google account for this. But I believe it should be generally safe if you do not share the app password to anyone

Q: Is this completed?

  A: No, its like 50%. I am left with exporting the results into an excel sheet

Q: When will it be done?

  A: idk, maybe when I am free from school?


