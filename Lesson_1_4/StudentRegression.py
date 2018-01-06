def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    from sklearn import linear_model
    ### name your regression reg
    reg = linear_model.LinearRegression()
    
    # Fit the train data
    reg.fit(ages_train, net_worths_train)
    
    return reg
