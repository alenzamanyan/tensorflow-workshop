## Առաջադրանք 1: Պատրաստում

### Քայլ 1:
Ստեղծիր անփոփոխ թենզոր (tensorflow constant) 3.2 արժեքով։ Վերագրիր **input**-ին։

### Քայլ 2:
Ստեղծիր tensorflow Variable (փոփոխական)։ Որպես սկզբնական արժեք, օգտագործիր 2.0։ Վերագրիր **weight**-ին ([documentation](https://www.tensorflow.org/api_docs/python/tf/Variable))։

### Քայլ 3:
Բազմապատկիր **weight**-ը **input**-ին և վերագրիր **output**-ին ([documentation](https://www.tensorflow.org/api_docs/python/tf/multiply))։

### Քայլ 4:
Տպիր գրաֆի բազմապատկման գործողությունը։ Ի՞նչ են input-ները։

### Քայլ 5:
Ստեղծիր գործողություն որը սկզբնական արժեքներ կտա փոփոխականներին [documentation](https://www.tensorflow.org/api_docs/python/tf/global_variables_initializer))։ Նկատիր որ այս դեպքում ունենք ընդամենը մեկ փոփոխական։

### Քայլ 6:
Ստեղծիր սեսիա եւ կատարիր գործողությունը որը ստեղծել էս **Քայլ 5**-ում։ **weight** փոփոխականը այժմ ունի սկզբնական արժեք (այն է 2.0)։

### Քայլ 7:
Կատարիր բազմապատկման գործողությունը սեսիայի մեջ։