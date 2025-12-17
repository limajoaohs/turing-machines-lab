import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Auto {
    public static void main(String[] args) {
        // Configurar o caminho do driver do navegador
        System.setProperty("webdriver.chrome.driver", "caminho/para/chromedriver");

        // Inicializar o WebDriver
        WebDriver driver = new ChromeDriver();

        try {
            // Abrir o site do Google
            driver.get("https://www.google.com");

            // Encontrar a barra de pesquisa e digitar um termo
            WebElement searchBox = driver.findElement(By.name("q"));
            searchBox.sendKeys("Automação com Java");

            // Enviar a pesquisa
            searchBox.submit();

            // Esperar os resultados carregarem e exibir o título da página
            Thread.sleep(2000); // Espera simples (não recomendada em projetos reais)
            System.out.println("Título da página: " + driver.getTitle());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // Fechar o navegador
            driver.quit();
        }
    }
}
