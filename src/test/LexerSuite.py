import unittest
from TestUtils import TestLexer

EOF = "<EOF>"
def testcase_seq():
    for i in range(100, 200):
        yield i

class LexerSuite(unittest.TestCase):
    sequence = testcase_seq()
    
    # -------------- Comment Test cases ------------------------ 
    def test_single_line_comment_end_with_newline(self):
        """test a line comment"""
        test_str = """## This is a comment
        """
        expected = f"\n,{EOF}" 
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_single_line_comment_end_with_EOF(self):
        """test a line comment"""
        test_str = """## This is a comment"""
        expected = f"{EOF}" 
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_inline_comment(self):
        """Test newline \n as statement terminator"""
        test_str = """bool a ##Hello
        """
        expected = f"bool,a,\n,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_comment_including_special_char_(self):
        """Test comment that contains # in its content"""
        test_str = "### This is a comment"
        expected = EOF
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_two_consecutive_comments(self):
        """Test comment that contains # in its content"""
        test_str = """## This is a comment
        ## This is another comment"""
        expected = f"\n,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_comment_spanning_mulitple_line(self):
        """Test comment that contains newline character to check for ending condition"""
        test_str = "##At\nstring name"
        expected = f"\n,string,name,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    #--------------String literals test cases-----------------
    def test_simple_string(self):
        """test simple string"""
        test_str = '"Yanxi Palace - 2018"'
        expected = f"Yanxi Palace - 2018,{EOF}"
        self.assertTrue(TestLexer.test(test_str,expected,next(self.sequence)))

    def test_string_with_single_quote(self):
        """test complex string"""
        test_str = """\"'isn''t\""""
        expected = f"'isn''t,{EOF}"
        self.assertTrue(TestLexer.test(test_str,",<EOF>",next(self.sequence)))

    def test_string_with_escape_backslash(self):
        """Test a correct string with escape character \\"""
        test_str = r'"This is a correct string with escape char \\"'
        expected = f"{test_str[1:-1]},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected,next(self.sequence)))

    # Single quote can be used in escaped and non escaped form
    def test_single_quote(self):
        """Test a correct string with escape character \'"""
        test_str = """string a <- "\\\'"
        """ 
        expected = f"string,a,<-,\\',\n,<EOF>"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_string_with_single_quote(self):
        """Test a correct string with escape character \'"""
        test_str = '"I\'am Thanh"'
        expected = f"I'am Thanh,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
 
    # Double quotes must be escaped with a leading single quote
    def test_string_with_inner_dbquote(self):
        """Test a correct string inner double quotes"""
        test_str = '''"Students said \'\"Do what you preach\'"\"'''
        expected = f"{test_str[1:-1]},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_unclosed_string(self):
        """Test unclosed string"""
        test_str = '''"This string is unclosed'''
        expected = f"Unclosed String: This string is unclosed"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
 
    def test_forward_slash_in_string(self):
        """Test unclosed string"""
        test_str = '''"/"'''
        expected = f"/,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_string_containing_newline_character(self):
        """Test a string that contains newline without being escaped"""
        test_str = '''"Hey\nBro"'''
        expected = f"Unclosed String: Hey"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_string_containing_unescaped_dquote(self):
        """Test an incorrect string that contains an unescapepd double quote"""
        test_str = '''"Hello "Thanh""'''
        expected = f"Hello ,Thanh,,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_empty_string(self):
        """Test empty string"""
        test_str = '''""'''
        expected = f",{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_unclosed_string_with_no_content(self):
        """Test unclosed string with open dquote only"""
        test_str = '''"'''
        expected = f"Unclosed String: "
        self.assertTrue(TestLexer.test(test_str, expected,next(self.sequence)))

    def test_string_containing_eof(self):
        """Test string that containg EOF"""
        test_str = '''"Hello'''
        expected = f"Unclosed String: Hello"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_unclosed_string_followed_by_number(self):
        test_str = '"Hello 123' 
        expected = f"Unclosed String: Hello 123" # instead of "Unclosed String: Hello"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_string_containing_invalid_escaped_char(self):
        """Test string with unknown escape character"""
        test_str = '"Hello\\yWorld"'
        expected = f"Illegal Escape In String: Hello\\y"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_string_containing_two_single_quotes(self):
        """Test string with two single quotes inside it"""
        test_str = """\"He said''Hello''.\""""
        expected = f"He said''Hello''.,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_illegal_single_quote_in_string(self):
        """Test a string containing a single quote without escaped and located at the end of input"""
        test_str = '''"thanh'"'''
        expected = f"Unclosed String: thanh'\""
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    ######################### Test number literals
    def test_integer_number(self):
        """Test integer number - a number without decimal and expornent part"""
        test_str = '12'
        expected = f"12,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_floating_with_decimal(self):
        """Test number with decimal part only"""
        test_str = '12.1'
        expected = f"12.1,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_floating_with_exponent(self):
        """Test number with exponent part only"""
        test_str = '12e10'
        expected = f"12e10,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_floating_with_negative_exponent(self):
        """Test number with negative exponent part only"""
        test_str = '12e-10'
        expected = f"12e-10,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_floating_with_positive_exponent(self):
        """Test number with positive exponent part only"""
        test_str = '12e+10'
        expected = f"12e+10,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_floating_with_multiple_positive_exponent(self):
        """Test number with positive exponent part only"""
        test_str = '12e++10'
        expected = f"12,e,+,+,10,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_floating_with_exponent_decimal(self):
        """Test number with both decimal and positive exponent part"""
        test_str = '12.2e10'
        expected = f"12.2e10,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_floating_with_dangling_decimal_part(self):
        """Test number with dangling decimal part"""
        test_str = '12.'
        expected = f"12.,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_floating_with_dangling_decimal_part_and_exponent(self):
        """Test number with positive exponent part only"""
        test_str = '12.e+10'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_decimal_point_with_no_integer_part(self):
        """Test a decimal number with an omitted integral part"""
        test_str = '.12'
        expected = f"Error Token ."
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_exponent_with_no_integer_part(self):
        """Test an exponent number with an omitted integral part"""
        test_str = 'e+10'
        expected = f"e,+,10,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_exponent_without_integer_part(self):
        """Test number with positive exponent part only"""
        test_str = '+10'
        expected = f"+,10,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_negative_number(self):
        """Test for a negative number with multiple leading minus sign"""
        test_str = '---23'
        expected = f"-,-,-,23,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence))) 
    
    def test_number_with_underscore_as_separator(self):
        test_str = '123_123'
        expected = f"123,_123,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence))) 
        
    #################Test for keywords
    def test_boolean_true(self):
        """test for true keyword"""
        test_str = 'true'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_boolean_false(self):
        """test for false keyword"""
        test_str = 'false'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_number_keyword(self):
        """test for number keyword"""
        test_str = 'number'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_bool_keyword(self):
        """test for bool keyword"""
        test_str = 'bool'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_string_keyword(self):
        """test for string keyword"""
        test_str = 'string'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_return_keyword(self):
        """test for return keyword"""
        test_str = 'return'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_var_keyword(self):
        """test for var keyword"""
        test_str = 'var'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_dynamic_keyword(self):
        """test for dynamic keyword"""
        test_str = 'dynamic'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_func_keyword(self):
        """test for func keyword"""
        test_str = 'func'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_for_keyword(self):
        """test for for keyword"""
        test_str = 'for'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_until_keyword(self):
        """test for until keyword"""
        test_str = 'until'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_by_keyword(self):
        """test for by keyword"""
        test_str = 'by'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_break_keyword(self):
        """test for break keyword"""
        test_str = 'break'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_continue_keyword(self):
        """test for continue keyword"""
        test_str = 'continue'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_if_keyword(self):
        """test for if keyword"""
        test_str = 'if'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_else_keyword(self):
        """test for else keyword"""
        test_str = 'else'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_elif_keyword(self):
        """test for elif keyword"""
        test_str = 'elif'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_begin_keyword(self):
        """test for begin keyword"""
        test_str = 'begin'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_end_keyword(self):
        """test for end keyword"""
        test_str = 'end'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_not_keyword(self):
        """test for not keyword"""
        test_str = 'not'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_and_keyword(self):
        """test for and keyword"""
        test_str = 'and'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_or_keyword(self):
        """test for or keyword"""
        test_str = 'or'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    ################### Test for operators
    def test_plus_operator(self):
        """test for + symbol"""
        test_str = '+'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_minus_operator(self):
        """test for - symbol"""
        test_str = '-'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_multiply_operator(self):
        """test for * symbol"""
        test_str = '*'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_division_operator(self):
        """test for / symbol"""
        test_str = '/'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_modulo_operator(self):
        """test for % symbol"""
        test_str = '%'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_equal_operator(self):
        """test for = symbol"""
        test_str = '='
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_assignment_operator(self):
        """test for <- symbol"""
        test_str = '<-'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_not_equal_operator(self):
        """test for != symbol"""
        test_str = '!='
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_lessthan_operator(self):
        """test for < symbol"""
        test_str = '<'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_greaterthan_operator(self):
        """test for > symbol"""
        test_str = '>'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_lst_eq_operator(self):
        """test for <= symbol"""
        test_str = '<='
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_gt_eq_operator(self):
        """test for >= symbol"""
        test_str = '>='
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_concat_operator(self):
        """test for ... symbol"""
        test_str = '...'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_compare_operator(self):
        """test for == symbol"""
        test_str = '=='
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    ################### Test for separators 
    def test_left_paren_separator(self):
        """test for left parenthesis separator"""
        test_str = '('
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_right_paren_separator(self):
        """test for right parenthesis separator"""
        test_str = ')'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_left_bracket_separator(self):
        """test for [ separator"""
        test_str = '['
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_right_bracket_separator(self):
        """test for ] separator"""
        test_str = ']'
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_comma_separator(self):
        """test for comma separator"""
        test_str = ','
        expected = f"{test_str},{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_newline_separator(self):
        """test for newline \n as whitespace character"""
        test_str = '\n'
        expected = f"\n,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    def test_newline_for_statement(self):
        """Test newline \n as statement terminator"""
        test_str = """bool a
        """
        expected = f"bool,a,\n,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    #------------ Identifier test cases -----------------------------------
    def test_id_starting_with_lowercase_character(self):
        """Test an identifier starting with a lowercase letter"""
        test_str = """string thanh23"""
        expected = f"string,thanh23,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_id_starting_with_uppercase_letter(self):
        """Test an identifier starting with a uppercase letter"""
        test_str = """dynamic Person"""
        expected = f"dynamic,Person,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_id_starting_with_underscore_letter(self):
        """Test an identifier starting with a uppercase letter"""
        test_str = """string _string"""
        expected = f"string,_string,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_id_starting_with_digit(self):
        """Attempt to declare an id starting with number 2"""
        test_str = """var 2pac"""
        expected = f"var,2,pac,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_id_containing_special_character(self):
        """Using undefined token to test the id"""
        test_str = """var 2pac$"""
        expected = f"var,2,pac,Error Token $"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_id_starting_containing_underscore_letter(self):
        """Test an identifier starting with a uppercase letter"""
        test_str = """dynamic dynamic_"""
        expected = f"dynamic,dynamic_,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))    
    
    def test_id_containing_concat_operator(self):
        test_str = """string hello...world"""
        expected = f"string,hello,...,world,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))  
    
    def test_id_redudant_with_a_keyword(self):
        test_str = """_func"""
        expected = f"_func,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))  
    
    def test_id_backslash(self):
        test_str = """string thanh\\n"""
        expected = f"string,thanh,Error Token \\"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))  

    def test_id_formed_2consecutive_keywords(self):
        test_str = """notnot"""
        expected = f"notnot,{EOF}" # instead of "not,not,<EOF>"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))  
    def test_id_case_sensitivity(self):
        test_str = """Func"""
        expected = f"Func,{EOF}" # instead of "func,<EOF>"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))   
    
    def test_comma(self):
        test_str = """number b[1, 2] <- [[1,2]]"""
        expected = f"number,b,[,1,,,2,],<-,[,[,1,,,2,],],{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))    
    
    def test_error_token(self):
        """Test an identifier starting with a uppercase letter"""
        test_str = """var thanh@gmail"""
        expected = f"var,thanh,Error Token @"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_concat_with_interfering_spaces(self):
        """Test an identifier starting with a uppercase letter"""
        test_str = """.\t.\t."""
        expected = f"Error Token ."
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_random(self):
        test_str = """# # This comment is erroneous"""
        expected = f"Error Token #"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_random2(self):
        test_str = """## This is a comment\n\t\t\n"""
        expected = f"\n,\n,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_random3(self):
        test_str = """## This is a comment\r\n"""
        expected = f"\n,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))

    def test_random4(self):
        test_str = """32.12jdk.123"""
        expected = f"32.12,jdk,Error Token ."
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_random5(self):
        test_str = """for_until_by"""
        expected = f"for_until_by,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_random6(self):
        test_str = """number age <- 2024 - 2002"""
        expected = f"number,age,<-,2024,-,2002,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    
    def test_random7(self):
        test_str = """string Full_name <- \"Thanh\" ... \"Le\""""
        expected = f"string,Full_name,<-,Thanh,...,Le,{EOF}"
        self.assertTrue(TestLexer.test(test_str, expected, next(self.sequence)))
    