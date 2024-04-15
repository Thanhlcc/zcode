import unittest
from TestUtils import TestParser
def testcase_seq():
    for i in range(200, 400):
        yield i
class ParserSuite(unittest.TestCase):
    sequence = testcase_seq()
    
    # Function declaration
    def test_func_null_paralist(self):
        input = """func main(     )
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_singleton_paralist(self):
        input = """func main(number args)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_multiple_paralist(self):
        input = """func main(string arg1, string arg2)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_implicit_decl_in_paralist(self):
        input = """func main(dynamic varargs)
        """
        expect = "Error on line 1 col 10: dynamic"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_paralist_omit_closing_paren(self):
        input = """func main (
        """
        expect = "Error on line 1 col 11: \n"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_paralist_omit_opening_paren(self):
        input = """func main )"""
        expect = "Error on line 1 col 10: )"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_paralist_omit_fulllist(self):
        input = """func main
        """
        expect = "Error on line 1 col 9: \n"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_body_empty(self):
        input = """func main()
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_body_return(self):
        input = """func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_body_block_statement(self):
        input = """func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_body_separator_one_newline(self):
        input = """func main()
        return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_body_separator_three_newline(self):
        input = """func main()
        
        
        return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_implicit_var_without_asm(self):
        input = """var name
        """
        expect = "Error on line 1 col 8: \n"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_implicit_var_with_asm(self):
        input = """var name <- "Thanh"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_implicit_dynamic_with_asm(self):
        input = """dynamic name <- "Thanh"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_implicit_dynamic_without_asm(self):
        input = """dynamic name
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_implicit_without_newline(self):
        input = "dynamic age"
        expect = "Error on line 1 col 11: <EOF>"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_implicit_with_array_id(self):
        input = """var nums[2] <- [1,2]
        """
        expect = "Error on line 1 col 8: ["
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_explicit_type_boolean(self):
        input = """bool flag
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_explicit_type_string(self):
        input = """string name 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_explicit_type_number(self):
        input = """number a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_explicit_without(self):
        input = """number age
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_explicit_with_asm(self):
        input = """number age <- 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_explicit_arrayid_zero_dim(self):
        input = """number nums[]
        """
        expect = "Error on line 1 col 12: ]"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_explicit_arrayid_with_onedim(self):
        input = """number nums[1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_explicit_arrayid_with_two_dimensions(self):
        input = """number nums[1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_var_explicit_arrayid_with_trailing_comma(self):
        input = """number nums[1,2,]
        """
        expect = "Error on line 1 col 16: ]"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence))) 
    
    def test_var_explicit_arrayid_with_leading_comma(self):
        input = """number nums[,]
        """
        expect = "Error on line 1 col 12: ,"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_ifstmt_zero_newline_bwt_condition_body(self):
        input = """func main() begin
            if (age > 18) print("you're in")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_ifstmt_one_newline_bwt_condition_body(self):
        input = """func main() begin
            if (age > 18) 
                print("you're in")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_ifstmt_three_newline_bwt_condition_body(self):
        input = """func main() begin
            if (age > 18) 
            
            
            print("you're in")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_ifstmt_body_omitted_end(self):
        input = """func main() begin
            if (age > 18)
        end
        """
        expect = "Error on line 3 col 8: end"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_ifstmt_body_omitted_EOF(self):
        input = """func main() begin
            if (age > 18)
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_ifstmt_condition_left_parenthesis_omitted(self):
        input = """func main() begin
            if age > 18) print("You're in")
        end
        """
        expect = "Error on line 2 col 15: age"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_ifstmt_condition_right_parenthesis_omitted(self):
        input = """func main() begin
            if (age > 18 print("You're in")
        end
        """
        expect = "Error on line 2 col 25: print"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_ifstmt_condition_both_parenthesis_omitted(self):
        input = """func main() begin
            if age > 18 print("You're in")
        end
        """
        expect = "Error on line 2 col 15: age"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_ifstmt_condition_omitted_empty_condition(self):
        input = """func main() begin
            if () print("You're in")
        end
        """
        expect = "Error on line 2 col 16: )"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_ifstmt_condition_omitted_completely(self):
        input = """func main() begin
            if print("You're in")
        end
        """
        expect = "Error on line 2 col 15: print"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence))) 

    def test_else_with_condition(self):
        input = """func main() begin
            if (age > 18) print("You're in")
            else (age <= 18) print("Let me grow you up")
        end
        """
        expect = "Error on line 3 col 17: ("
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_simple_else(self):
        input = """func main() begin
            if (age > 18) print("You're in")
            else print("Let me grow you up")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_else_without_preceding_if(self):
        input = """func main() begin
            else print("Let me grow you up")
        end
        """
        expect = "Error on line 2 col 12: else"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_else_with_two_interfering_stmt(self):
        input = """func main() begin
            if (age > 18) print("You're in")
            print("Cumming baby")
            else print("Let me grow you up")
        end
        """
        expect = "Error on line 4 col 12: else"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_else_with_one_following_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in")
            else 
                print("Let me grow you up")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_else_with_three_following_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in")
            else


            print("Let me grow you up")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))

    
    def test_else_body_omitted_end(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in")
            else

        end
        """
        expect = "Error on line 6 col 8: end"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_else_body_omitted_EOF(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in")
            else
        """
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_separator_between_if_else_zero_newline(self):
        input = """func main() begin
            if (age > 18) print("You're in") else print("let me grow u up")
        end
        """
        expect = "Error on line 2 col 45: else"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_separator_between_if_else_multiple_newline(self):
        input = """func main() begin
            if (age > 18) print("You're in") 
            
            
            else print("let me grow u up")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    def test_if_one_elif_body_separator_zero_newline(self):
        input = """func main() begin
            if (age > 18) print("You're in") 
            elif (age > 15) print("You're not of my interest")
        end
        """  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_if_one_elif_body_separator_one_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif (age > 15) 
                print("You're not of my interest")
        end
        """  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))

    
    def test_if_one_elif_body_separator_three_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif (age > 15)


            print("You're not of my interest")
        end
        """  
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))

  
    def test_if_one_elif_body_omitted_end(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif (age > 15)
        
        end
        """  
        expect = "Error on line 6 col 8: end"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))

   
    def test_if_one_elif_body_omitted_EOF(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif (age > 15)
        """  
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))


    def test_if_one_elif_condition_leftP_omitted(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif age > 15)
                print("You're not of my interest")
        """  
        expect = "Error on line 4 col 17: age"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))

   
    def test_if_one_elif_condition_rightP_omitted(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif (age > 15
                print("You're not of my interest")
        """  
        expect = "Error on line 4 col 26: \n"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_if_one_elif_condition_both_omitted(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif age > 15
                print("You're not of my interest")
        """  
        expect = "Error on line 4 col 17: age"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_if_one_elif_condition_empty(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif ()
                print("You're not of my interest")
        """  
        expect = "Error on line 4 col 18: )"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_if_one_elif_condition_omitted(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif
                print("You're not of my interest")
        """  
        expect = "Error on line 4 col 16: \n"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_if_two_elif_zero_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif ( age > 15 ) print("You're not of my interest") elif ( age > 10 ) print("cut")
        
        end
        """   
        expect = "Error on line 4 col 65: elif"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_if_two_elif_one_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif ( age > 15 ) print("You're not of my interest")
            elif ( age > 10 ) print("cut")
        end
        """   
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_if_two_elif_three_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif ( age > 15 ) print("You're not of my interest")


            elif ( age > 10 ) print("cut")
        end
        """   
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    

    def test_if_two_leading_elif_two_stmt_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif ( age > 15 ) 
                print("You're not of my interest")
                print("You're not of my interest")
            elif ( age > 10 ) print("cut")
        end
        """   
        expect = "Error on line 7 col 12: elif"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_if_elif_else_zero_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif ( age > 15 ) print("You're not of my interest") else print("You're not of my interest")
        end
        """   
        expect = "Error on line 4 col 65: else"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    def test_if_elif_else_one_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif ( age > 15 ) print("You're not of my interest")
            else print("You're not of my interest")
        end
        """   
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))  
    
    def test_if_elif_else_three_newline(self):
        input = """func main() begin
            if (age > 18) 
                print("You're in") 
            elif ( age > 15 ) print("You're not of my interest") 
            
            
            else print("You're not of my interest")
        end
        """   
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))  
    
    def test_loop_control_variable(self):
        input = """func main() begin
            var i <- 0
            for i until i < 10 by 1 print("Hello")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_loop_invalid_condition(self):
        input = """
        func main() begin
            var i <- 0
            for i until return 3 by 1 
                print("Hello")
        end
        """
        expect = "Error on line 4 col 24: return"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    
    def test_loop_simple_update_expression(self):
        input = """
        func main() begin
            var i <- 0
            for i until i < 100 by update() 
                print("Hello")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_loop_empty_body(self):
        input = """
        func main() begin
            var i <- 0
            for i until i < 100 by update()

        end
        """
        expect = "Error on line 6 col 8: end"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_loop_complex_body(self):
        input = """
        func main() begin
            var i <- 0
            for i until i < 100 by update() begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (isPrime(x)) writeString("Yes")
                else writeString("No")
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    
    def test_separator_loop_body_and_update_expr_three_newline(self):
        input = """
        func main() begin
            var i <- 0
            for i until i < 100 by update()
            

            print("Hello World")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    def test_separator_loop_body_and_update_expr_no_newline(self):
        input = """
        func main() begin
            var i <- 0
            for i until i < 100 by update() print("Hello World")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))        
    def test_loop_until_omitted(self):
        input = """
        func main() begin
            var i <- 0
            for i by update() 
                print("Hello World")
        end
        """
        expect = "Error on line 4 col 18: by"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    
    def test_loop_by_omitted(self):
        input = """
        func main() begin
            var i <- 0
            for i until i < 100
                print("Hello World")
        end
        """
        expect = "Error on line 4 col 31: \n"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    
    def test_loop_until_and_by_on_different_line(self):
        input = """
        func main() begin
            var i <- 0
            for i until i < 100 
            by update() print("Hello World")
        end
        """
        expect = "Error on line 4 col 32: \n"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    
    def test_asm_lhs_variableId(self):
        input = """
            func main() begin
                number age

                age <- 20
            end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_asm_lhs_variableId(self):
        input = """
            func main() begin
                number nums[1,2]

                nums <- [[1,2]]
            end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_asm_lhs_arrayId(self):
        input = """
            func main() begin
                number age

                age <- 20
            end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_continue_no_endline(self):
        input = """
            func main() begin
                for i until 10 by 1 
                    if (i == 2) continue end
    """
        expect = "Error on line 4 col 41: end"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_continue_one_endline(self):
        input = """
            func main() begin
                for i until 10 by 1 
                    if (i == 2) continue 
            end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_continue_three_endline(self):
        input = """

                    func main() begin
                for i until 10 by 1 
                    if (i == 2) continue 



            end

    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_break_no_endline(self):
        input = """
            func main() begin
                for i until 10 by 1 
                    if (i = 2) break end
    """
        expect = "Error on line 4 col 37: end"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_break_one_endline(self):
        input = """
            func main() begin
                for i until 10 by 1 
                    if (i = 2) break
            end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_break_three_endline(self):
        input = """

                    func main() begin
                for i until 10 by 1 
                    if (i == 2) break 



            end

    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_return_with_no_newline(self):
        input = """
            func main() return"""
        expect = "Error on line 2 col 30: <EOF>"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_return_with_one_newline(self):
        input = """
            func main() return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    def test_return_with_two_newline(self):
        input = """
            func main() return


        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_return_with_value_no_newline(self):
        input = """
            func main() return 1"""
        expect = "Error on line 2 col 32: <EOF>"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_return_with_value_one_newline(self):
        input = """
            func main() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_block_begin_without_end(self):
        input = """
            func main() begin
    
                
                var a <- 12
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    
    def test_block_begin_without_following_newline(self):
        input = """
            func main() begin var a <- 12 
            end
        """
        expect = "Error on line 2 col 30: var"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    
    def test_block_no_newline_after_end(self):
        input = """
            func main() begin
                var a <- 12
            end"""
        expect = "Error on line 4 col 15: <EOF>"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    
    def test_block_three_newline_after_end(self):
        input = """
            func main() begin
                begin
                    dynamic name <- "Thanh"
                end

                
                print("hello")
            end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    
    def test_funccall_id_test(self):
        input = """
        number nums[2] <- [1,2]
        func main() begin
            nums[1]()
        end
        """
        expect = "Error on line 4 col 19: ("
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_funccall_id_valid(self):
        input = """
        func foo()
        func main() begin
            foo()
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_funccall_paramlist_one(self):
        input = """
        func foo()
        func main() begin
            foo(1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_funccall_paramlist_two(self):
        input = """
        func foo()
        func main() begin
            foo(koo(), boo())
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))    
    
    def test_funccall_paramlist_error_sep(self):
        input = """
        func main() begin
            foo(boo() foo()) 
        end
        """
        expect = "Error on line 3 col 22: foo"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_func_paralist_invalid_sep(self):
        input = """
            func main(number a / string b)
        """
        expect = "Error on line 2 col 31: /"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    
    def test_empty_array_init(self):
        input = """number nums <- []
        """
        expect = "Error on line 1 col 16: ]"
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))
    def test_invalid_numbervar_loop(self):
        input = """
            func main() begin
                for foo() until 10 by 1
                    print("Hello")
            end
        """
        expect = "Error on line 3 col 23: ("
        self.assertTrue(TestParser.test(input,expect,next(self.sequence)))

    