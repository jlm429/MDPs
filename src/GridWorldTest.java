package burlap;

import burlap.behavior.policy.Policy;
import burlap.behavior.policy.PolicyUtils;
import burlap.behavior.singleagent.Episode;
import burlap.behavior.singleagent.auxiliary.EpisodeSequenceVisualizer;
import burlap.behavior.singleagent.auxiliary.StateReachability;
import burlap.behavior.singleagent.auxiliary.valuefunctionvis.ValueFunctionVisualizerGUI;
import burlap.behavior.singleagent.learning.tdmethods.QLearning;
import burlap.behavior.singleagent.planning.stochastic.policyiteration.PolicyIteration;
import burlap.behavior.singleagent.planning.stochastic.valueiteration.ValueIteration;
import burlap.behavior.valuefunction.ValueFunction;
import burlap.domain.singleagent.gridworld.GridWorldDomain;
import burlap.domain.singleagent.gridworld.GridWorldTerminalFunction;
import burlap.domain.singleagent.gridworld.GridWorldVisualizer;
import burlap.domain.singleagent.gridworld.state.GridWorldState;
import burlap.mdp.core.Domain;
import burlap.mdp.core.state.State;
import burlap.mdp.singleagent.SADomain;
import burlap.mdp.singleagent.environment.Environment;
import burlap.mdp.singleagent.environment.SimulatedEnvironment;
import burlap.statehashing.simple.SimpleHashableStateFactory;
import java.util.ArrayList;
import java.util.List;

//TODO: fix gui hang bug
public class GridWorldTest {

  SADomain domain;
  Environment env;
  GridWorldState initialState;

  public GridWorldTest(int width, int height) {
    //define the problem
    GridWorldDomain gwd = new GridWorldDomain(width, height);
    gwd.setMapToFourRooms();
    gwd.setTf(new GridWorldTerminalFunction(width-1, height-1));
    gwd.setProbSucceedTransitionDynamics(0.7); //stochastic transitions with 0.7 success rate
    domain = gwd.generateDomain();
    initialState = new GridWorldState(0, 0);
    env = new SimulatedEnvironment(domain, initialState);
  }

  public void runQLearner() {
    //create a Q-learning agent
    QLearning agent = new QLearning(domain, 0.99, new SimpleHashableStateFactory(), 1.0, 1.0);
    //run 100 learning episode and save the episode results
    System.out.println("running q-learner");
    List<Episode> episodes = new ArrayList();
    for(int i = 0; i < 100; i++){
      episodes.add(agent.runLearningEpisode(env));
      env.resetEnvironment();
    }
    System.out.println("q-learner finished");
    Policy p = agent.planFromState(initialState);
    String outputPath="";
    PolicyUtils.rollout(p, initialState, domain.getModel()).write(outputPath + "QL");
    simpleValueFunctionVis((ValueFunction)agent, p, initialState, domain, new SimpleHashableStateFactory());
    //visualize the completed learning episodes
    //new EpisodeSequenceVisualizer(GridWorldVisualizer.getVisualizer(gwd.getMap()), domain, episodes);
  }

  public void runPI() {
    //PI
    PolicyIteration planner = new PolicyIteration(domain, 0.99, new SimpleHashableStateFactory(), .01, 100, 100);
    Policy p = planner.planFromState(initialState);
    String outputPath="";
    PolicyUtils.rollout(p, initialState, domain.getModel()).write(outputPath + "PI");
    simpleValueFunctionVis((ValueFunction)planner, p, initialState, domain, new SimpleHashableStateFactory());
  }

  public void runVI() {
    //VI
    ValueIteration planner = new ValueIteration(domain, .99, new SimpleHashableStateFactory(), .01, 1000);
    Policy p = planner.planFromState(initialState);
    String outputPath="";
    PolicyUtils.rollout(p, initialState, domain.getModel()).write(outputPath + "VI");
    simpleValueFunctionVis((ValueFunction)planner, p, initialState, domain, new SimpleHashableStateFactory());
  }

  public static void simpleValueFunctionVis(ValueFunction valueFunction, Policy p, GridWorldState initialState, SADomain domain, SimpleHashableStateFactory hashingFactory){
    List<State> allStates = StateReachability.getReachableStates(initialState,
      domain, hashingFactory);
    ValueFunctionVisualizerGUI gui = GridWorldDomain.getGridWorldValueFunctionVisualization(
      allStates, 12, 12, valueFunction, p);
    gui.initGUI();
  }

  public static void main(String[] args) {
    GridWorldTest test = new GridWorldTest(11,11);
    //test.runPI();
    //test.runVI();
    test.runQLearner();
  }
}
