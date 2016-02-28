import java.util.Iterator;

/**
 * @author oscar
 * @desc 两种不同的解析json方式
 *           1. net.sf.json   2. org.json
 *
 */
public class JsonParser {
	
	public static void main(String[] args){
		
		String str = "{\"response\":{\"data\":[{\"address\":\"南京市游乐园\",\"province\":\"江苏\",\"district\":\"玄武区\",\"city\":\"南京\"}]},\"status\":\"ok\"}";
		String resp = orgParserJson(str);
		
		System.out.println(resp);
		
		System.out.println(netParserJson(str));
	}
	
	private static String orgParserJson(String str){
		
		org.json.JSONObject json  = new org.json.JSONObject(str);
		
		org.json.JSONObject data = json.getJSONObject("response");
		org.json.JSONArray info  = data.getJSONArray("data");
		
		StringBuilder resp = new StringBuilder();
		
		for(int i=0; i<info.length();i++){
			org.json.JSONObject ss = new org.json.JSONObject(info.get(i).toString());
			for(String val:ss.keySet()){
				resp.append(val.toString()).append("=").append(ss.get(val).toString()).append("\n");
			}
		}
		return resp.toString();
	}
	
	private static String netParserJson(String str){
		net.sf.json.JSONObject  dataJson= net.sf.json.JSONObject.fromObject(str);
		net.sf.json.JSONObject  response= dataJson.getJSONObject("response");
		
		net.sf.json.JSONArray json = response.getJSONArray("data");
		
		
		String resp = new String();
		for(int i=0; i<json.size(); i++){
			net.sf.json.JSONObject info = json.getJSONObject(i);
			resp = info.get("province").toString()+"\n"+info.get("district").toString()+"\n"+info.get("city").toString();
		}
		
		return resp;
	}
		
		
		
		
		

		
		
	
	
}
