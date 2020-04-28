import java.util.*;

public class RoyalRumble {
  public int charToInt(char c){
    switch(c){
      case 'I':
        return 1;
      case 'V':
        return 5;
      case 'X':
        return 10;
      case 'L':
        return 50;
      default:
        return 0;
    }
  }
  public List<String> getSortedList(List<String> names) {
    String roman = "str";
    String roman1 = "str";
    String tmp = "str";
    List<String> result = new ArrayList<String>();
    Collections.sort(names); 
    
    for(int i = 1; i < names.size(); i++){
      if(names.get(i).toString().charAt(0) == names.get(i - 1).toString().charAt(0)){
        roman = (names.get(i)).toString().split("\\s+")[1];
        roman1 = (names.get(i - 1)).toString().split("\\s+")[1];
        
        System.out.println(romanToInt(roman));
        System.out.println(romanToInt(roman1));
        if(Integer.valueOf(romanToInt(roman1)) > Integer.valueOf(romanToInt(roman))){
          tmp = names.get(i - 1);
          names.set(i - 1, names.get(i));
          names.set(i, tmp);
        }
      } else {
        if((int) names.get(i).toString().charAt(0) < (int) names.get(i - 1).toString().charAt(0)){
          tmp = names.get(i - 1);
          names.set(i - 1, names.get(i));
          names.set(i, tmp);
        }
      }
    }
      
    System.out.println(names);
    System.out.println("THIS IS THE RESULT");
    return result;
  }

  public int romanToInt(String romanChar) {
    int total = 0;
    for(int i = 0; i < romanChar.length(); i++){
      int cur = charToInt(romanChar.charAt(i));
      if( (i+1) < romanChar.length()){
        int next = charToInt(romanChar.charAt(i + 1));
        if(cur < next){
          total += (next - cur);
          i++;
        }else{
          total += cur;
        }
      }
      else{
        total += cur;
      }
    }
    return total;
  }

}
