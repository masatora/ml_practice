import java.io.File
import scala.io.Source
import org.apache.log4j.Logger
import org.apache.log4j.Level
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.rdd._
import org.apache.spark.mllib.recommendation.{ ALS, Rating, MatrixFactorizationModel }

Logger.getLogger("org").setLevel(Level.OFF)
Logger.getLogger("com").setLevel(Level.OFF)
System.setProperty("spark.ui.showConsoleProgress", "false")
Logger.getRootLogger().setLevel(Level.OFF)

val data = sc.textFile(new File("data", "u.data").toString)
val X = data.map(_.split("\t").take(3)).map{
    case Array(user, movie, rating) => Rating(user.toInt, movie.toInt, rating.toDouble)
}
val als = ALS.train(X, 5, 20, 0.1)
val recomMovieId = readLine()
als.recommendUsers(recomMovieId, 10).foreach{
    r => println(r.user + " => " + r.rating)
}