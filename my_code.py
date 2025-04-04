import pytest

def fix_phone_num(phone_num_to_fix):
  # Remove all non-digit characters
  cleaned_num = "".join(filter(str.isdigit, phone_num_to_fix))
  
  # Validate input length
  if len(cleaned_num) != 10:
        raise ValueError("Invalid phone number format")
    
  # given "5125558823". Split the parts, then recombine and return
  area_code = cleaned_num[0:3] # 512 (first three digits)
  three_part = cleaned_num[3:6] # 555 (next three digits)
  four_part = cleaned_num[6:] # # 8823 (last four digits)
  
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'

def test_handle_non_standard_formats():
  assert fix_phone_num("555-442-9876") == "(555) 442 9876"
  assert fix_phone_num("(321) 654 3333") == "(321) 654 3333"

def test_fix_phone_num_invalid_input():
    with pytest.raises(ValueError):  
        fix_phone_num("51") 

    with pytest.raises(ValueError):
        fix_phone_num("555-442-98761") 

    with pytest.raises(ValueError):
        fix_phone_num("ABCDE12345")  

      



   

