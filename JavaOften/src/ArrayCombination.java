/**
 * 1.�ݹ������㷨
 * 2. �ݹ�����㷨
 * 3. ��̬�滮����㷨
 * 
 */
//�����㷨
//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.List;
//import java.util.Stack;
// 
////public class ArrayCombination {
// 
//public class ArrayCombination {
//    private static char[] is = new char[] {'5', '6', '7', '8', '9'};
//    private static String[] sList = new String[] {"a","b","c","d","e"};
////    Stack<String> stack= new Stack<String>();
//    
////    for(int i=0; i<sList.length; i++){
////    	stack.push(sList[i]);
////    }
//    
//    private static int total;
//    private static int m = 2;
//    public static void main(String[] args) {
//        List<Integer> iL = new ArrayList<Integer>();
//        new ArrayCombination().plzh("", iL,  m);
//        System.out.println("total : " + total);
//    }
//    private void plzh(String s, List<Integer> iL, int m) {
//        if(m == 0) {
//            System.out.println(s);
//            total++;
//            return;
//        }
//        List<Integer> iL2;
//        ArrayList<String> sList1 = new ArrayList<String>(Arrays.asList(sList));
//        
//        for(int i = 0; i < sList.length; i++) {
//            iL2 = new ArrayList<Integer>();
//            iL2.addAll(iL);
//            if(!iL.contains(i)) {
//                String str = s + sList[i];
//                iL2.add(i);
//    //        sList1.remove(i);
//                
//                System.out.println("kaifei\t"+str+"aaa\t"+iL2);
//                plzh(str, iL2, m-1);
//            }
//        }
//    }
//}
//����㷨
import java.util.ArrayList;
import java.util.List;

public class ArrayCombination {
 public static void main(String[] args) {
//  String[] a = { "1", "2", "3"};
  String[] b = new String[]{"1","2","3","4"};
  int num = 2;
  //test
  ArrayCombination tp = new ArrayCombination();
  for (String obj : tp.combine(b, num)) {
   System.out.println(obj);
  }
  //test
 }
 
 /**
  * ʵ�ֵ��㷨
  * @param a ��������
  * @param num MѡN�� N�ĸ���
  * @return
  */
 private List<String> combine(String[] a, int num) {
  List<String> list = new ArrayList<String>();
  StringBuffer sb = new StringBuffer();
  String[] b = new String[a.length];
  for (int i = 0; i < b.length; i++) {
   if (i < num) {
    b[i] = "1";
   } else
    b[i] = "0";
  }

  int point = 0;
  int nextPoint = 0;
  int count = 0;
  int sum = 0;
  String temp = "1";
  while (true) {
   // �ж��Ƿ�ȫ����λ���
   for (int i = b.length - 1; i >= b.length - num; i--) {
    if (b[i].equals("1"))
     sum += 1;
   }
   // ������λ��������
   for (int i = 0; i < b.length; i++) {
    if (b[i].equals("1")) {
     point = i;
     sb.append(a[point]);
     count++;
     if (count == num)
      break;
     else{
    	 sb.append("\001");
     }
    }
   }
   // ������ֵ�б��������
   list.add(sb.toString());

   // ����������numλȫ��Ϊ1 �˳�
   if (sum == num) {
    break;
   }
   sum = 0;

   // �޸Ĵ������ҵ�һ��10���01
   for (int i = 0; i < b.length - 1; i++) {
    if (b[i].equals("1") && b[i + 1].equals("0")) {
     point = i;
     nextPoint = i + 1;
     b[point] = "0";
     b[nextPoint] = "1";
     break;
    }
   }
   // �� i-point��Ԫ�ص�1��ǰ�ƶ� 0�����ƶ�
   for (int i = 0; i < point - 1; i++)
    for (int j = i; j < point - 1; j++) {
     if (b[i].equals("0")) {
      temp = b[i];
      b[i] = b[j + 1];
      b[j + 1] = temp;
     }
    }
   // ��� StringBuffer
   sb.setLength(0);
   count = 0;
  }
  // 
//  System.out.println("���ݳ��� " + list.size());
  return list;

 }

}


//��̬�滮 ����㷨
//public class ArrayCombination {
//  public static void main(String[] args) {
//      int[] sList=new int[]{1,2,3,4};
//      String str="";
//      //��3��������ϸ���
//      count(0,str,sList,2);
//     
//  }
//
//  private static void count(int i, String str, int[] sList,int n) {
//      if(n==0){
//          System.out.println(str);
//          return;
//      }
//      if(i==sList.length){
//          return;
//      }
//      count(i+1,str+sList[i]+",",sList,n-1);
//      count(i+1,str,sList,n);
//  }
//}
 