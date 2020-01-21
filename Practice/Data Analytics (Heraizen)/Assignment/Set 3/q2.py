while(True):
    ch=input("a.Write into the file\nb.Read from the file\nc.Exit\n")
    if ch=="a":
        fs=open("Demonetization.txt","w")
        fs.write("On 8 November 2016, the Government of India announced the demonetization of all Rs.500 and Rs.1,000 banknotes of the Mahatma Gandhi Series. It also announced the issuance of new Rs.500 and Rs.2,000 banknotes in exchange for the demonetised banknotes. The Prime minister of India Narendra Modi claimed that the action would curtail the shadow economy and reduce the use of illicit and counterfeit cash to fund illegal activity and terrorism.\nAccording to a 2018 report from the Reserve Bank of India, approximately '99.3%' of the demonetised banknotes, or Rs.15.30 lakh crore (15.3 trillion) of the Rs.15.41 lakh crore that had been demonetised, were deposited with the banking system. The banknotes that were not deposited were only worth Rs.10,720 crore (107.2 billion), leading analysts to state that the effort had failed to remove black money from the economy. The BSE SENSEX and NIFTY 50 stock indices fell over 6 percent on the day after the announcement. The move reduced the country's industrial production and its GDP growth rate.\nInitially, the move received support from several bankers as well as from some international commentators. The move was also criticised as poorly planned and unfair, and was met with protests, litigation, and strikes against the government in several places across India. Debates also took place concerning the move in both houses of the parliament.")
        fs.close()
        print("File Created Successfully!")
    elif ch=="b":
        try:
            fs=open("Demonetization.txt","r")
            for line in fs:
                print(line)
            fs.close()
        except FileNotFoundError:
            print("File not yet created. Please create the file before accessing it")
    else:
        print("You have chosen to exit the operation. Thanks.")
        exit()


