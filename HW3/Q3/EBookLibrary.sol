pragma solidity ^0.5.0;
import "./CustomERC20.sol";


/**
 * @title EBookLibrary
 * A smart contract for renting books
 */

contract EBookLibrary is CustomERC20{
    
    event Deposit(address indexed sender, uint256 amount);
    event Withdrawal(address indexed recipient, uint256 amount);


    //***********************************************
    //********* Variables, Structs, Enums ***********
    //***********************************************

    //address of the admin
    address payable admin;
    
    // fee that a user should pay to become a premium user
    uint premiumFee;


    //access duration of books
    uint accessDuration;
	
	
	enum AccountType {regular, premium}
	
	//address of users to their account type. by default regular
	//in solidity enums if something is not set it has the first defined value in the enum
	mapping (address => AccountType) accoutTypes;
	
	

    enum BookGenre {fiction, novel, poetry, psychology}


    //Book specification
    struct Book {
        bool isValid; //needed in order to check where the book is added,
                    //in solidity mapping if something is not set it has the value which is false for boolean
        uint accessFee;
        BookGenre bookGenre;
        
    }

    struct rentInfo{
        address payable renter;
        uint startTime;
        bool available;
		
    }
    
    //Rented books id to rental information
    mapping (uint => rentInfo) rentedBooks;
    
    
    //Mapping book id to book specification
    mapping (uint => Book) books;



    //***********************************************
    //****************** modifiers ******************
    //***********************************************
    /**
     * @dev Reverts if msg sender is not the admin
     */
    modifier onlyAdmin() {
        require(msg.sender == admin);
        _;
    }


    /**
     * @dev Reverts if book's access duration has not ended
     * @param bookId, book to be checked
     */
    modifier onlyAfterAccessDuration(uint bookId) {
        require(now > rentedBooks[bookId].startTime + accessDuration);
        _;
    }

    /**
     * @dev Reverts if the book does not exist
     * @param bookId, book to be checked
     */
    modifier onlyIfbookExists(uint bookId) {
        require(books[bookId].isValid == true);
        _; 
    }


    //*************************************************
    //****************** Constructor ******************
    //*************************************************

    /**
     * @dev Constructor, sets admin and rental period
     * @param _accessDuration, rental period of books
     * @param _premiumFee, the fee that user should pay to becom a premium user
     */
    constructor(uint _accessDuration , uint _premiumFee)public{
        premiumFee = _premiumFee;
        admin = msg.sender;
        accessDuration = _accessDuration;
    }



    //***********************************************
    //****************** functions ******************
    //***********************************************
	
	/**
     * @dev deposit ELTs
     */
    function deposit() 
    public 
    payable {
        _mint(msg.sender, msg.value);
         emit Deposit(msg.sender, msg.value);
  }
	

    /**
     * @dev Add a book to books mapping
     * Be carefull to set isValid and available to true
     * @param bookId, ID of the book
     * @param bookGenre, genre of the book
     * @param accessFee, accessFee of the book
     */
    function addbook(uint bookId,uint bookGenre,uint accessFee) 
    onlyAdmin
    public{
	//TODO
	//
    }
	
	
	
	/**
     * @dev change the account type of a user 
     * transfer premiumFee in ELTs from user account to admin account
     */
    function changeToPremiun()
    public 
    payable{
    //TODO
	//
    }
	
	
	
    /**
     * @dev Rent a book and give ELTs for the accessFee to the admin(Be careful to cover premium user rule)
     * @param bookId ID of the book
     */
    function accesss(uint bookId) payable 
    onlyIfbookExists(bookId) 
    public{
	//TODO
    //
    }


    /**
     * @dev revokes the renter's access to the book if the access duration has ended.
     * only admin can call this function
     * @param bookId ID of the book
     */
    function revoke(uint bookId) 
    onlyAdmin()
    onlyAfterAccessDuration(bookId)
    public{
	//TODO
	//
    }


 

    /**
     * @dev Get the state of a book
     * you can use this function for debugging purposes
     * @param bookId, ID of the book
     * @return bookGenre, genre of the book
     * @return accessFee, accessFee of the book
     * @return startTime, Start time of reting period
     * @return renter, Address of the renter
     * @return available, availablity of the book
     */
    function getBook(uint bookId) public view 
    returns(  BookGenre ,uint ,uint ,address ,bool){
        Book memory book = books[bookId];
        return (
            book.bookGenre,
            book.accessFee,
            rentedBooks[bookId].startTime,
            rentedBooks[bookId].renter,
            rentedBooks[bookId].available
            );
    }
	
	
	
	/**
     * @dev any user that wants to exit this library can call this function in order to withdraw his/her ELTs
     * @param amount, the amount of ELTs that user wants to convert to Ether
     */
    function withdraw(uint amount) public {
        require(balanceOf(msg.sender) >= amount);
        address payable recipient = msg.sender;
        recipient.transfer(amount);
        _burn(msg.sender, amount);
        emit Withdrawal(recipient, amount);
  }
	

}                              


                         