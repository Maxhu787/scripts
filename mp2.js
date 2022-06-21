const Person = function (firstAndLast) {
    let fullName = firstAndLast;
    this.getFullName = function () {
        return fullName;
    };

    this.getFirstName = function() {
        return fullName.split(' ')[0];
    };

    this.getLastName = function() {
        return fullName.split(' ')[1];
    };

    this.setFirstName = function(name) {
        fullName = name + " " + fullName.split(' ')[1]
    };

    this.setLastName = function(name) {
        fullName = fullName.split(' ')[0] + " " + name;
    };

    this.setFullNAme = function(name) {
        fullName = name; 
    }
};

const bob = new Person('Bob Ross');
bob.getFullName();
