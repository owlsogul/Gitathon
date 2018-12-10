import java.io.IOException;
import java.net.URL;
import java.security.cert.Certificate;
import java.security.cert.CertificateEncodingException;
import javax.net.ssl.HttpsURLConnection;
import javax.security.cert.CertificateException;
public class Hc {
    public static void main(String[] args) throws IOException, CertificateEncodingException, CertificateException {
        if (args == null || args.length == 0) {
            System.err.println("url parameter not suppplied. ");
            System.exit(0);
        }
         
        URL url;
         
        url = new URL(args[0]);
        HttpsURLConnection con = (HttpsURLConnection) url.openConnection();
        System.out.println("Response Code : " + con.getResponseCode());
        System.out.println("Cipher Suite : " + con.getCipherSuite());
        System.out.println("\n");
        Certificate[] certs = con.getServerCertificates();
        for (Certificate cert : certs) {
            javax.security.cert.X509Certificate c = javax.security.cert.X509Certificate.getInstance(cert.getEncoded());
            System.out.println("\tCert Dn : " + c.getSubjectDN());
            System.out.println("\tIssuer Dn : " + c.getIssuerDN());
            System.out.println("\n");
        }
         
        con.disconnect();
    }
}
